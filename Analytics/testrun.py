from Analytics.analytics import content, wordvec


def init():
    content.getContent()
    token = wordvec.getToken()
    wordvec.learnVector(token)

init()