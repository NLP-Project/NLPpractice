from gensim.models import Word2Vec
from Analytics.analytics.config import db
from Analytics.analytics import wordvec

from konlpy.tag import Twitter




def dbQuery_insert(sql,insertData):
    conn = db.getConnection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql,insertData)
            conn.commit()
    finally:
        conn.close()


def dbQuery(sql, param) :
    result = []
    conn = db.getConnection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, param)
            _result = cursor.fetchall()

            for i in range(len(_result)):
                result.append(_result[i])

    except Exception as ex:  # 에러 종류
        print('Error Break : ', ex, " in Function dbQuery ")  # ex는 발생한 에러의 이름을 받아오는 변수

    finally:
        conn.close()
        return result


def articleSimilarity(article_1, article_2):
    model = Word2Vec.load('./analytics/vector.model')
    return model.wv.similarity(article_1, article_2)




# 기사 간의 유사도를 측정하는 function
# 초기에 1번만 실행
def initBtwArticleSimilarity():
    sql = "SELECT id,content FROM article"
    param = []
    result = dbQuery(sql, param)
    '''
    print(result[0]) # ( (id,content) )
    print(result[0][0]) # id
    print(result[0][1]) # content
    '''

    for i in range(len(result) - 1):
        j = i + 1
        sql = "SELECT * FROM article_representation_noun WHERE id = "
        param = str(result[i][0])
        article1_rep_noun = dbQuery(sql , param)
        # print(article1_rep_noun)
        # [(20, '보드', '주행', '전동', '타이어', '제품')]

        while j < len(result):
            param = str(result[j][0])
            article2_rep_noun = dbQuery(sql , param)
            print("article2_rep_noun : " , article2_rep_noun)
            # [(21, '보드', '주행', '전동', '타이어', '제품')]

            similarity_value = 0
            loop_per_cnt = 5

            try :
                for a in range(loop_per_cnt):
                    for b in range(loop_per_cnt):
                        similarity_value += articleSimilarity(article1_rep_noun[0][a + 1],article2_rep_noun[0][b + 1])

                insertQuery = "INSERT INTO article_similarity_value(article1, article2, similarity_value) VALUES ( %s , %s, %s )"
                insertData = (str(result[i][0]) , str(result[j][0]) , str(similarity_value / 25 ))
                dbQuery_insert(insertQuery, insertData)

                j += 1
            except Exception as ex:  # 에러 종류
                print('Error Break : ', ex , " in Function initBtwArticleSimilarity")  # ex는 발생한 에러의 이름을 받아오는 변수



def insertRepresentationNoun():
    selectSQL= " SELECT id, content FROM article"
    param = []
    selectResult = dbQuery(selectSQL, param)

    try:
        for i in range(len(selectResult)):
            mostNounResult = wordvec.getMostNoun(selectResult[i][1])

            sql = "INSERT INTO article_representation_noun(id, noun_1, noun_2, noun_3, noun_4, noun_5) VALUES ( %s, %s, %s, %s, %s, %s) "
            insertData = ( str(selectResult[i][0]), mostNounResult[0][0][0], mostNounResult[0][1][0], mostNounResult[0][2][0] ,mostNounResult[0][3][0] ,mostNounResult[0][4][0] )
            dbQuery_insert(sql, insertData)

    except Exception as ex:  # 에러 종류
        print('Error Break : ', ex, " in Function insertRepresentationNoun ")  # ex는 발생한 에러의 이름을 받아오는 변수

    finally:
        print(" End :: Function insertRepresentationNoun ")


def initTraingModel():
    doc_ko = db.getArticle()
    t = Twitter()

    noun_token = []
    for i in range(len(doc_ko)):
        tokens_ko = t.morphs(doc_ko[i])
        noun_token.append(tokens_ko)

    model = Word2Vec(noun_token, min_count=1, iter=1000)
    model.save('./analytics/vector.model')


def recArticleList(userid) : # rec is recommend
    selectSQL = "SELECT article_id FROM like_list WHERE user_id = %s"
    param = (str(userid))
    liked_list_by_user = dbQuery( selectSQL , param)

    article_list = []

    for i in range(len(liked_list_by_user)):
        article_list.append(liked_list_by_user[i][0])

    # 좋아요한 글들간의 유사성 값을 측정
    size = len(article_list)
    denominator = size * (size-1) / 2 # denominator means 분모

    sum = 0

    for i in range(size-1):
        j = i + 1
        while j < size:
            selectSQL = "SELECT similarity_value FROM article_similarity_value WHERE article1 = %s and article2 = %s"
            param = (article_list[i], article_list[j])

            selectResult = dbQuery(selectSQL, param)
            sum += selectResult[0][0]
            j += 1

    if sum != 0 :
        pivot_value = sum / denominator
    else :
        pivot_value = 0.05


    for i in range(size):
        selectSQL = "SELECT article2 FROM article_similarity_value WHERE article1 = %s and similarity_value >= %s"
        param = (article_list[i], pivot_value)

        selectResult = dbQuery(selectSQL, param)

        for j in range(len(selectResult)):
            article_list.append(selectResult[j][0])

    article_list = list(set(article_list))

    return article_list



'''
# 새로운 Article로 모델 만들때 사용
def_set.initTraingModel()
'''

'''
# 글에서 대표 명사 추출
import Analytics.analytics.def_set as a
a.insertRepresentationNoun()
'''

'''
# 글간의 유사도 측정을 위한 설정
import Analytics.analytics.def_set as b
b.initBtwArticleSimilarity()
'''



