from gensim.models import Word2Vec
from konlpy.corpus import kobill
from konlpy.tag import Twitter
from config import db


def getToken():
	token = []
	t = Twitter()
	mostNounList = []
	articleList = db.getArticle()
	for i in range(len(articleList)):
		token.append(t.morphs(articleList[i]))
		mostNounList.append(getMostNoun(articleList[i], t))
	print mostNounList
	return token

def learnVector(wordToken):
	model = Word2Vec.load('./vector.model')
	model.Word2Vec(wordToken, min_count = 1, iter = 1000)
	model.save('./vector.model')

def getMostNoun(article, twitter):
	mostNoun = []
	cntNoun = twitter.nouns(article)
	tmpCount = []
	for i in range(len(cntNoun)):
		if len(cntNoun[i])>1:
			tmpCount.append(cntNoun[i])
	mostNoun.append(Counter(tmpCount).most_common(5))
	return mostNoun