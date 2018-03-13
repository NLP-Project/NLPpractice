# -*- coding: utf-8 -*-

from gensim.models import Word2Vec
from konlpy.corpus import kobill
import dbConnection as db

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

# print(doc_ko)
# print(len(doc_ko))


from konlpy.tag import Twitter;

t = Twitter()

noun_token = []

rep_noun = []
from collections import Counter

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


print('*********************************')

model = Word2Vec(noun_token, iter=1000)

priority_arr = []

print(model.most_similar('맥아'))
for i in range(len(noun_token)):  # 문장개수
    for j in range(len(noun_token[i])):  # 해당문장의 단어수
        print(noun_token[i][j])
        similarity = (int)(abs(model.wv.similarity('플랫폼', noun_token[i][j])) * 100)
        _a = t.pos(noun_token[i][j])
        if _a[0][1] == "Noun" and _a[0][1] == "에서" and len(_a[0][0]) > 1:
            _tuple = noun_token[i][j], similarity
            priority_arr.append(_tuple)

from operator import itemgetter

priority_arr = list(set(priority_arr))
priority_arr = sorted(priority_arr, key=itemgetter(1), reverse=True)  # sort by Second Value
print(priority_arr)






def LoadModel() :
    return Word2Vec.load('./word2vec.model')


# model.save('./word2vec.model')
# model = LoadModel()



def article_similarity(article_1, article_2):
    return (int)(abs(model.wv.similarity(article_1,article_1)) * 100)



