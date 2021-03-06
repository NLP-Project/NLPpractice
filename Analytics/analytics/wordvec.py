from gensim.models import Word2Vec
from konlpy.tag import Twitter
from Analytics.analytics.config import db
from collections import Counter



def getToken():
    token = []
    t = Twitter()
    mostNounList = []
    articleList = db.getArticle()
    for i in range(len(articleList)):
        token.append(t.morphs(articleList[i]))
        mostNounList.append(getMostNoun(articleList[i]))
    return token

def learnVector(wordToken):
	model = Word2Vec.load('./analytics/vector.model')
	model.train(wordToken, total_examples=model.corpus_count, epochs=model.iter)
	model.save('./analytics/vector.model')


def getMostNoun(article):
    twitter = Twitter()
    mostNoun = []
    cntNoun = twitter.nouns(article)
    tmpCount = []
    for i in range(len(cntNoun)):
        if len(cntNoun[i]) > 1 :
            tmpCount.append(cntNoun[i])
    mostNoun.append(Counter(tmpCount).most_common(5))
    return  mostNoun
