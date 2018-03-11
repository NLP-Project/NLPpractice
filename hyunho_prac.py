from gensim.models import Word2Vec
from konlpy.corpus import kobill


files_ko = kobill.fileids()


doc_ko = [ '26개 주사위로 이뤄진 정육면체' , '단 0.38초만에 맞추는 로봇이 나왔다.' ]



from konlpy.tag import Twitter; t = Twitter()

noun_token = []
for i in range( len( doc_ko ) ) :
    tokens_ko = t.morphs( doc_ko[i] )
    noun_token.append( tokens_ko )


print( "noun_token")
print( noun_token )
print()


print('*********************************')

model = Word2Vec( noun_token , min_count = 1 , iter = 1000 )

priority_arr = []

for i in range(len(noun_token)):  # 문장개수
    for j in range(len(noun_token[i])):  # 해당문장의 단어수
        similarity = (int)(abs(model.wv.similarity('주사위', noun_token[i][j])) * 100)
        _a = t.pos(noun_token[i][j])
        if _a[0][1] == "Noun" and len(_a[0][0]) > 1:
            _tuple = noun_token[i][j], similarity
            priority_arr.append(_tuple)

from operator import itemgetter

priority_arr = sorted(priority_arr, key=itemgetter(1), reverse=True)  # sort by Second Value
print(priority_arr)