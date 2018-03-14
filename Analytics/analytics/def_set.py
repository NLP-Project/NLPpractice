from gensim.models import Word2Vec
from Analytics.analytics.config import db



def dbQUery(sql) :
    result = []
    conn = db.getConnection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            _result = cursor.fetchall()

            for i in range(len(_result)):
                result.append(_result[i])

    finally:
        conn.close()
        return result


def article_similarity(article_1, article_2):
    model = Word2Vec.load('./analytics/vector.model')
    return model.wv.similarity(article_1, article_2)
