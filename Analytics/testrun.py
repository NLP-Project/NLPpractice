from analytics import content, wordvec

def run():
	content.getContent()
	token = wordvec.getToken()
	if len(token) > 0 :
		wordvec.learnVector(token)

run()