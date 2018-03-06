
from gensim.models import Word2Vec
from konlpy.tag import Kkma
from konlpy.utils import pprint
from konlpy.tag import Kkma


kkma = Kkma()


content_array = "핸드폰을 잃어버렸더니 세상의 일부와 단절되었다. 그 대신 발견한 다른 세상의 일부.01 수첩이간단한 메모용으로 쓰려고 상자 구석에서 꺼낸 수첩에는 동거인들의 전화번호와 기차표 시간과 좌석번호, 네이버 지도 대용 손그림 약도, 잊어버리면 안되는 일들 같은 게 빼곡하다. 알림장을 보는 기분.02 사진이아낌없이 주는 옆방사람들은 공기계 핸드폰과 카드를 빌려주었다. 처음 써보는 안드로이드형 핸드폰으로 사진을 몇 장 찍었다. '이렇게 나오겠지'하면 저렇게 나온다. 오래 써오던 아이폰 카메라와는 다른 느낌의 사진이 찍혀서, 새로운 시선을 획득한 기분★03 세상이아직 해가 지기 전.월요일의 일몰을 보며 집으로 가는 길.세상과 잠깐 차단되었지만 그렇게 나쁘지는 않다.지하철에서 멀뚱히 새카만 창밖을 바라보는 사람이 나뿐이어도 나쁘지 않다. 얼마나 그 작은 스마트폰에 의존하고 살았는지 하나씩 알게 되는 시간.(그렇지만 곧 카톡이 필요하겠지. 통신사에서 개통을 하고 있겠지.) 현대카드 정태영 회장이 2월 28일 페이스 북에 가슴 떨리는 글을 남겼다. 그리고 곧이어 오는 10월 9일 서울 고척 스카이돔에서 23번째 슈퍼콘서트로 ‘샘 스미스’를 초대한다고 발표했다. data-app   data-app애플 크리스마스 광고는 겨울 특유의 건조함을 우연한 만남의 상상력으로 감성적으로 바꿨다는 평가를 받는다. 이 광고가 이런 극찬을 받을 수 있었던 이유는 단연 BGM 덕분이었다. 세계 스마트폰을 양분하고 있는 삼성과 애플을 비교하는 글을 보면 항상 삼성에겐 감성이 부족하다고 한다. 아무리 추운 날씨에 제멋대로 꺼지고 한 달 월급의 대부분을 가져가는 고가의 핸드폰이지만, 혹시라도 떨어뜨리면 수 십만 원이 추가로 깨지는 연약하디 연약한 액정을 가지고 있지만 애플이라는 이유로 사람들은 아이폰을 위해 기꺼이 지갑을 연다. 그리고 갤럭시를 쓰는 사람을 은연중에 무시한다.이런 걸 보면 소비 심리라는 게 참 묘하다. 기업들이 기를 쓰고 브랜딩을 하는 이유가 여기에 있을 것이다. 튼튼하고 값싸면 잘 팔릴 거 같지만 이러한 법칙은 모든 물품에 적용되지 않는다. 사람 속이란 걸 이해하기가 이렇게 어렵다. data-app   data-app다시 샘 스미스 이야기로 돌아오면 애플의 크리스마스 광고에 들어간 노래는 2017년 11월 3일에 발표한 샘 스미스의 두 번째 앨범 <The Thrill Of It All>의 9번째 트랙인 ‘Palace’라는 곡이다.  이 앨범의 자켓을 보면 살짝 놀랄 수밖에 없는데 다소 통통했던 샘 스미스가 피골이 상접한 꼴로 멍하니 위를 응시하고 있기 때문이다. 무슨 심경의 변화가 있었는지 살이 쏙 빠진 샘 스미스가 슬픈 노래를 부르니 그 우울함과 쓸쓸함이 시각적으로 전해지는 것 같다. 10월 달에 샘 스미스의 멜랑콜리함이 서울에서 증폭되겠구나란 생각을 하니까 벌써부터 가을의 쓸쓸함이 느껴진다. 그걸 느끼기 위해 티켓팅 성공을 기원한다!! Sam Smith - PalaceMy head is filled with ruinsdata-app내 머릿속은 폐허로 가득해 data-appMost of them are built with youdata-app대부분 너로 인해 만들어졌어 data-appNow the dust no longer movesdata-app이제 쌓이는 먼지는 더 이상 움직이지 않아 data-appDon’t disturb the ghost of youdata-app너라는 유령이 방해하지 않으니data-appMmmdata-app   data-appThey are empty, they are worndata-app텅 비었다 다 닳아버렸어 data-appTell me what we built this fordata-app말해줄래 우린 무엇을 위해 이 성을 만들 걸까 data-appOn my way to something moredata-app더 많은 무엇을 형해 가는 길 위에도data-appYou’re that one I can’t ignoredata-app넌 내가 지나쳐갈 수 없는 한 사람인데 data-appMmmdata-app   data-appI’m gonna miss youdata-app그리울 거야data-appI still caredata-app여전히 그러니까 data-appSometimes I wish we never built this palacedata-app때론 난 우리가 이 성을 만들지 않았으면 하고 바라겠지data-appBut real love is never a waste of timedata-app그러나 진정한 사랑은 낭비가 아니야 data-appMmmdata-app   data-appYeah I know just what you’re sayingdata-app그래 알아 무슨 말인지data-appAnd I regret ever complainingdata-app내가 했던 모든 불평을 후회해data-appAbout this heart and all its breakingdata-app이 마음과 부서져간 조각들 data-appIt was beauty we were makingdata-app그건 우리가 만든 아름다움이었는데data-appMmmdata-app   data-appAnd I know we’ll both move ondata-app그리고 우리가 둘 다 나아가리라는 걸 알아 data-appYou’ll forgive what I did wrongdata-app넌 내가 잘못했던 그때를 용서하겠지 data-appThey will love the better youdata-app그들이 너를 더 아름답게 사랑해주겠지data-appBut I still own the ghost of youdata-app하지만 난 아직 너라는 유령에 사로잡혀 있는 걸data-appMmmdata-app   data-appI’m gonna miss youdata-app그리울 거야 data-appI’m still theredata-app여전히 거기 있으니data-appSometimes I wish we never built this palacedata-app가끔 난 우리가 이 성을 만들지 않았으면 하고 바라겠지data-appBut real love is never a waste of timedata-app하지만 진정한 사랑은 낭비가 아닌 걸data-app  data-app   data-appI’m gonna miss youdata-app그리울 거야 data-appI’m still theredata-app여전히 거기 있으니data-appSometimes I wish we never built this palacedata-app가끔 난 우리가 이 성을 만들지 않았으면 하고 바라겠지data-appBut real love is never a waste of timedata-app하지만 진정한 사랑은 낭비가 아닌 걸data-appBut real love is never a waste of timedata-app하지만 진정한 사랑은 낭비가 아닌 걸 * 스타트업 디자이너로 종사하며 겪었던 프로젝트의 고민과 그에 따른 결과물들을 공유하고자 합니다.본 글은 2017년 2월에 진행된 데일리(데일리호텔)의 홈 배너 개선 프로젝트를 기재한 것입니다.*첫인상은 한번 각인되면 쉽게 바뀌지 않는다는 말을 한 번쯤은 들어보셨을 텐데요. 표정, 옷매무새 등으로 자신을 어떻게 표현하느냐에 따라 첫인상이 좌지우지됩니다. 그렇다면 앱(App)에서의 첫인상은 어디서 결정될까요?바로 '홈 배너'입니다.'데일리호텔'앱 2.0 버전에는 기존에 없던 홈화면이 추가되면서 마케팅 성격의 배너 영역이 확대되었습니다.(아래 이미지 참고) 해서 데일리호텔의 첫인상을 책임질 새로운 배너 가이드의 필요성을 느끼게 됩니다.01 무엇을 고려해야 할까?홈화면에는 '데일리호텔/데일리고메' 버튼이 새로 생성되었습니다. 사실상 두 버튼이 예약을 위한 제일 첫 단의 경로였기 때문에 이 버튼의 주목성을 방해하지 않는 선에서 레이아웃 및 톤 앤 매너를 정의해야 했어요. 또한 영역이 커진 만큼 주목도가 높아지기 때문에 유저가 지루함을 느껴서는 안 되었죠.때문에 크게 이러한 목표를 두었습니다.첫 번째. 디자인 개선두 번째. 프로덕트(UI)와의 조화위 두가지를 기반으로 데일리의 브랜드 디자인 키워드에 맞춰 아래와 같은 구체적인 방향을 설정하였습니다.02 타사 써칭 및 분석data-app  가이드를 잡기에 앞서, 타사의 경우 홈배너를 어떻게 활용하고 있는지 조사가 필요했습니다. 많은 자료들을 모아 분석해본 결과 데일리의 경우 크게 세 가지 형태로 배너를 표현할 수 있음을 도출할 수 있었죠.첫 번째. 텍스트 + 오브젝트를 함께 살리는 안두 번째. Full Image를 사용하여 하단에 텍스트 박스를 기재하는 안세 번째. 이미지에 Dim처리를 한 후 텍스트를 기재하는 안단순히 디자인의 심미성 영역을 넘어서 많이 사용되는 호텔과 레스토랑 이미지를 실제로 적용시킬 수 있는지의 판단 또한 필요했습니다. 호텔 내부 이미지의 경우 누끼(*오브젝트만 남기고 배경을 지우는 작업)를 딸 수 없는 경우가 많았기 때문이죠.03 데일리와 어울리는 컬러는?data-app  배너의 레이아웃이 얼추 뼈대를 드러내는 시점에 함께 적용시킬 수 있는 컬러를 찾아야 했습니다. 앞서 말했듯이 예약 경로인 버튼의 주목성을 해치지 않는 톤 앤 매너를 유지하고, 마케팅적인 성격보다는 추천의 성격을 띠기 위해 차분한 톤이 필요했습니다.04 결과data-app  최종적으로 반영된 사항은 아래와 같았습니다.1. 호텔/레스토랑 프로모션 배너 -> 누끼 혹은 그라데이션으로 이미지 처리2. 브랜드 메시지 배너 -> Full Image에 Black Dim 처리3. 누끼를 딸 수 있는 이미지 사용 권장4. 따뜻한 파스텔톤의 컬러 사용5. 워딩 Black/White Color로 통일해서 위와 같은 결과물을 얻을 수 있었습니다. 전과 후 배너 비교를 해보니 새삼 구 배너가 너무 많은 메시지 전달을 하려는 성향이 있었음을 느끼게 되었어요.(반성..) 또한, 이번 배너 개선 프로젝트를 통해 디자인 심미성뿐만이 아니라 많은 부분을 얻을 수 있었습니다.마치며생각보다 길어진 프로젝트였지만 프로덕트와 마케팅적인 관점에서 많은 부분을 감안하고 작업을 진행한 만큼 모두가 만족할 수 있는 결과물이었습니다. 또한 홈화면의 홈배너 개선 후 많은 유저분들이 단순한 마케팅 메시지가 아닌 '라이프스타일 추천'을 받을 수 있어서 좋다는 피드백을 주셨습니다. 즉, 본 개선 작업으로 인해 브랜드 톤 앤 매너 또한 개선된 샘이었죠.앞으로도 데일리호텔이 추구하는 방향을 유저에게 전달하기 위한 많은 과제가 놓여있다는 것을 알고 있습니다. 어떻게 하면 더 전달할 수 있을지, 더 가까워질 수 있을지, 더 특별한 삶을 보낼 수 있도록 도울 수 있을지 고민하는 디자이너가 되도록 하겠습니다! 감사합니다 :)"


#content_array = "발열은 LTE폰의 숙명 ㅠㅠ"

print('*********************************')
tokenized_contents = kkma.pos(content_array)
noun_token = []
temp = []


for j in range( len( tokenized_contents )) :
     #if(( tokenized_contents[j][1] == 'NNG' ) or ( tokenized_contents[j][1] == 'NNP')):
        temp.append( tokenized_contents[j][0])

noun_token.append( temp )
print( noun_token )

model = Word2Vec(noun_token, size = 100 , min_count=1)
print( model )

print( model.most_similar(positive=["핸드폰"] , topn = 3 ))




'''
from gensim.models import Word2Vec



tokenized_contents= [['배터리', '핸드폰', '노트북', '맥북']]

model = Word2Vec(tokenized_contents, min_count=1)

print(model)

#embedding_model = Word2Vec(tokenized_contents, size=100, window = 2, min_count=50, workers=4, iter=100, sg=1)
#print( embedding_model )

print(model.most_similar(positive=["배터리"], topn=100))





# 우선 단어 임베딩을 위한 코퍼스를 만든다. 코퍼스는 리스트의 리스트 형태로 구현되어야 한다.
# 내부 리스트는 하나의 문장을 이루는 단어 열이 된다.

from nltk.corpus import movie_reviews
sentences = [list(s) for s in movie_reviews.sents()]
print(sentences[0])
# 다음으로 이 코퍼스를 입력 인수로 하여 Word2Vec 클래스 객체를 생성한다. 이 시점에 트레이닝이 이루어진다.
from gensim.models import Word2Vec
model = Word2Vec(sentences[0])

# model.save('./gid.txt')
# model = Word2Vec.load('./gid.txt')

# 트레이닝이 완료되면 init_sims 명령으로 필요없는 메모리를 unload 시킨다.
model.init_sims(replace=True)


# similarity : 두 단어의 유사도 계산
# most_similar : 가장 유사한 단어를 출력


print(model.most_similar(positive = ['drive']))
print()
'''