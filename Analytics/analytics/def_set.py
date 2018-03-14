from gensim.models import Word2Vec
from Analytics.analytics.config import db


def dbQUery_insert(sql):
    print(sql)
    conn = db.getConnection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()
    finally:
        conn.close()


def dbQUery(sql) :
    result = []
    conn = db.getConnection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            _result = cursor.fetchall()

            for i in range(len(_result)):
                result.append(_result[i])

    finally:
        conn.close()
        return result


def article_similarity(article_1, article_2):
    model = Word2Vec.load('./analytics/vector.model')
    return model.wv.similarity(article_1, article_2)




# 기사 간의 유사도를 측정하는 function
# 초기에 1번만 실행
def init_btw_article_similarity():
    sql = "SELECT id,content FROM article"
    result = dbQUery(sql)
    '''
    print(result[0]) # ( (id,content) )
    print(result[0][0]) # id
    print(result[0][1]) # content
    '''

    for i in range(len(result) - 1):
        j = i + 1
        sql = "SELECT * FROM article_representation_noun WHERE id = "
        param = str(result[i][0])
        article1_rep_noun = dbQUery(sql + param)
        # print(article1_rep_noun)
        # [(20, '보드', '주행', '전동', '타이어', '제품')]

        while j < len(result):
            param = str(result[j][0])
            article2_rep_noun = dbQUery(sql + param)
            # print(article2_rep_noun)
            # [(21, '보드', '주행', '전동', '타이어', '제품')]

            if result[j][0] == 38:
                print("지금 DB에 id값이 38까지 밖에 없어서 임시로 Break")
                break

            similarity_value = 0
            loop_per_cnt = 5

            for a in range(loop_per_cnt):
                for b in range(loop_per_cnt):
                    similarity_value += article_similarity(article1_rep_noun[0][a + 1],
                                                                   article2_rep_noun[0][b + 1])

            insertQuery = "INSERT INTO article_similarity_value(article1, article2, similarity_value) VALUES ("
            dbQUery_insert(
                insertQuery + str(result[i][0]) + "," + str(result[j][0]) + "," + str(similarity_value) + ")")

            j += 1

