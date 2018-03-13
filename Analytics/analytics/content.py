import requests
from analytics.config import db 
from bs4 import BeautifulSoup as Soup
from analytics.url import getUrl
from selenium import webdriver

baseUrl = 'https://brunch.co.kr'

def getContent():
	urlList = getUrl("it")
	titleList = []
	contentList = []
	for i in range(len(urlList)):
		url = baseUrl + urlList[i]
		r = requests.get(url)
		if r.status_code == 200:
			soup = Soup(r.text, "html.parser")
			title = soup.find("title").get_text()
			content = soup.find_all(class_='wrap_item item_type_text')
			tmp_content = ''
			for j in range(len(content)):
				tmp_content += content[j].get_text('data-app')
			contentList.append(tmp_content.replace("data-app", ""))
			titleList.append(title)
	if len(titleList) > 0:
		db.insertArticle(titleList, contentList, urlList)
