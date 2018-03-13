import requests
from bs4 import BeautifulSoup as Soup
from selenium import webdriver


driver = webdriver.PhantomJS('./phantomjs')

base_url = 'https://brunch.co.kr'
category = {
	"travel" : "/keyword/지구한바퀴_세계여행?q=g",
	"webtoon" : "/keyword/그림·웹툰?q=g",
	"issue" : "/keyword/시사·이슈?q=g",
	"it" : "/keyword/IT_트렌드?q=g",
	"photo" : "/keyword/사진·촬영?q=g",
	"movie" : "/keyword/취향저격_영화_리뷰?q=g",
	"book" : "/keyword/오늘은_이런_책?q=g",
	"music" : "/keyword/뮤직_인사이드?q=g"
}
path_array = []
title_array = []
content_array = []
sentence_array = []

def getUrl(path_array, title_array):
	driver.get(base_url + category["it"])
	html = driver.page_source
	soup = Soup(html, "html.parser")
	path_list = soup.find_all(class_ = "link_post")
	for i in range(len(path_list)):
		path_array.append(path_list[i].get('href'))
		title_array.append(path_list[i].find(class_ = 'tit_subject').get_text())

def getContent(path_array, content_array, sentence_array):
	for path_index in range(len(path_array)):
		url = base_url + path_array[path_index]
		r = requests.get(url)
		if r.status_code == 200:
			soup = Soup(r.text, "html.parser")
			content_list = soup.find_all(class_='wrap_item item_type_text')
			tmp_content = ''
			for i in range(len(content_list)):
				tmp_content += content_list[i].get_text('data-app')

			content_array.append(tmp_content)

	for i in range(len(content_array)):
		content_array[i] = content_array[i].replace("data-app", "")
		print('***************' + title_array[i] + '******************')
		print(content_array[i])

getUrl(path_array, title_array)
getContent(path_array, content_array, sentence_array)