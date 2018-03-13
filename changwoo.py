from gensim.models import Word2Vec
from konlpy.corpus import kobill
import dbConnection as db
from collections import Counter

files_ko = kobill.fileids()

doc_ko = [] # array 선언


try:
    with db.connection.cursor() as cursor:
        sql = "SELECT content FROM article"
        cursor.execute(sql)
        result = cursor.fetchall()

        for i in range(len(result)):
            doc_ko.append(result[i][0])
finally:
    cursor.close()
    # print("End")
    # db.connection.close()


# print(doc_ko)
# print(len(doc_ko))
from konlpy.tag import Twitter; t = Twitter()

noun_token = []

rep_noun = []
for i in range( len( doc_ko ) ) :
    tokens_ko = t.nouns(doc_ko[i]) #의미단어 검출
    # print(tokens_ko)
    # print(len(tokens_ko[0]))
    for j in range(len(tokens_ko)):
        if len(tokens_ko[j]) >1:
            # print(tokens_ko[j])
            noun_token.append(tokens_ko[j])
            cnt = Counter(noun_token)

    rep_noun.append(cnt.most_common(5))


try:
    with db.connection.cursor() as cursor:
        for i in range(len(rep_noun)):
            value = rep_noun[i]
            sql = 'INSERT INTO article_representation_noun(noun_1,noun_2,noun_3,noun_4,noun_5) VALUES (%s,%s,%s,%s,%s)'
            cursor.execute(sql,(value[0][0],value[1][0],value[2][0],value[3][0],value[4][0]))
    db.connection.commit()
    print(cursor.lastrowid)
    # 1 (last insert id)
finally:
    db.connection.close()


# print(noun_token)
# cnt = Counter(noun_token)
# print(cnt)