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



from konlpy.tag import Twitter;
t = Twitter()

noun_token = []
rep_noun = [] # rep is representation

from collections import Counter
for i in range( len( doc_ko ) ) :
    tokens_ko = t.morphs(doc_ko[i])
    noun_token.append(tokens_ko)

    cnt_tokens_ko = t.nouns(doc_ko[i]) #의미단어 검출
    tmp_arr = []
    for j in range(len(cnt_tokens_ko)):
        if len(cnt_tokens_ko[j]) >1:
            tmp_arr.append(cnt_tokens_ko[j])
            cnt = Counter(tmp_arr)
    noun_token.append(tmp_arr)
    rep_noun.append(cnt.most_common(5))


'''

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

'''




print( "noun_token")
print(noun_token[0])
print()



print('*********************************')

model = Word2Vec( noun_token , min_count = 1 , iter = 1000 )
print(model.wv.vocab)
priority_arr = []


for i in range(len(noun_token)):  # 문장개수
    for j in range(len(noun_token[i])):  # 해당문장의 단어수
        similarity = (int)(abs(model.wv.similarity('해마다', noun_token[i][j])) * 100)
        _a = t.pos(noun_token[i][j])
        if _a[0][1] == "Noun" and _a[0][1] == "에서" and len(_a[0][0]) > 1:
            _tuple = noun_token[i][j], similarity
            priority_arr.append(_tuple)


from operator import itemgetter

priority_arr = sorted(priority_arr, key=itemgetter(1), reverse=True)  # sort by Second Value
# print(priority_arr)






def LoadModel() :
    return Word2Vec.load('./word2vec.model')


# model.save('./word2vec.model')
# model = LoadModel()



def article_similarity(article_1, article_2):
    return abs(model.wv.similarity(article_1,article_2))

