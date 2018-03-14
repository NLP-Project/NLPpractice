from Analytics.analytics import content, wordvec, def_set

def run():
    content.getContent()
    token = wordvec.getToken()
    print(token)
    # if len(token) > 0 :
    #     wordvec.learnVector(token)



# 기사 간의 유사도를 측정하는 function
def cal_btw_article_similarity():
    sql = "SELECT id,content FROM article"
    result = def_set.dbQUery(sql)
    return result



# run()


result = cal_btw_article_similarity()
print("========")
print(result[0]) # ()
print(result[0][0]) # id
print(result[0][1]) # content

