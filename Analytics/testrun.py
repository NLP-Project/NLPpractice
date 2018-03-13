from analytics import content, wordvec

def run():
	content.getContent()
	token = wordvec.getToken()
	wordvec.learnVector(token)