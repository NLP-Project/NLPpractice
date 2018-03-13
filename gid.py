




def LoadModel() :
    return Word2Vec.load('./word2vec.model')


# model.save('./word2vec.model')
model = LoadModel()






def article_similarity(article_1, article_2):
    return (int)(abs(model.wv.similarity(article_1,article_1)) * 100)
