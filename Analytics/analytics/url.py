import requests
from Analytics.analytics.config import db
from bs4 import BeautifulSoup as Soup
from selenium import webdriver
from collections import Counter

driver = webdriver.PhantomJS('./analytics/phantomjs')
baseUrl = 'https://brunch.co.kr'

categoryList = {
	"travel" : "/keyword/지구한바퀴_세계여행?q=g",
	"webtoon" : "/keyword/그림·웹툰?q=g",
	"issue" : "/keyword/시사·이슈?q=g",
	"it" : "/keyword/IT_트렌드?q=g",
	"photo" : "/keyword/사진·촬영?q=g",
	"movie" : "/keyword/취향저격_영화_리뷰?q=g",
	"book" : "/keyword/오늘은_이런_책?q=g",
	"music" : "/keyword/뮤직_인사이드?q=g"
}

def getUrl(category):
    driver.get(baseUrl + categoryList[category])
    html = driver.page_source
    soup = Soup(html, "html.parser")
    tmpPath = soup.find_all(class_ = "link_post")
    pathList = []
    for i in range(len(tmpPath)):
        pathList.append(tmpPath[i].get('href'))
    driver.quit()
    lastUrl = db.getArticleHistory(category)
    for i in range(len(pathList)):
        if lastUrl == pathList[i]:
            pathList = pathList[0:i]
            break
    if len(pathList) > 0 :
        db.updateHistory(category, pathList[0])
    return pathList

