from Analytics.analytics import content, wordvec

def run():
    content.getContent()
    token = wordvec.getToken()
    print(token)
    # if len(token) > 0 :
    #     wordvec.learnVector(token)


# run()


print("========")

