from gensim.models import Word2Vec
from konlpy.tag import Twitter
from analytics.config import db
from collections import Counter


def getToken():
	token = []
	t = Twitter()
	mostNounList = []
	articleList = db.getArticle()
	for i in range(len(articleList)):
		token.append(t.morphs(articleList[i]))
		mostNounList.append(getMostNoun(articleList[i], t))
	print(mostNounList)
	return token

def learnVector(wordToken):
	model = Word2Vec.load('./analytics/vector.model')
	model.train(wordToken)
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