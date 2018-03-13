from gensim.models import Word2Vec
from konlpy.corpus import kobill
from konlpy.tag import Twitter
from Analytics.analytics.config import db
from collections import Counter


# noinspection PyUnresolvedReferences
def getToken():
    t = Twitter()
    token = []
    mostNounList = []
    articleList = db.getArticle()
    for i in range(len(articleList)):
        token.append(t.morphs(articleList[i]))
        mostNounList.append(getMostNoun(articleList[i],t))
    return token


def learnVector(wordToken):
    model = Word2Vec.load('./vector.model')
    model.train(wordToken)
    model.save('./vector.model')


def getMostNoun(article, twitter):
    mostNoun = []
    cntNoun = twitter.nouns(article)
    tmpCount = []
    for i in range(len(cntNoun)):
        if len(cntNoun[i]) > 1 :
            tmpCount.append(cntNoun[i])
    mostNoun.append(Counter(tmpCount).most_common(5))
    return  mostNoun
