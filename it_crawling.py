# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as Soup
from selenium import webdriver
from konlpy.tag import Kkma
from konlpy.utils import pprint
from collections import Counter


kkma = Kkma()
driver = webdriver.PhantomJS('./phantomjs')


base_url = 'https://brunch.co.kr'
path_array = []
title_array = []
content_array = []
sentence_array = []

def getUrl(path_array, title_array):
	driver.get('https://brunch.co.kr/keyword/IT_%ED%8A%B8%EB%A0%8C%EB%93%9C?q=g')
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
		content_array[i].replace("data-app", "", content_array[i].count("data-app"))
		sentence_list = content_array[i].split('.')
		sentence = []
		for j in range(len(sentence_list)):
			each_sentence = [sentence_list[j]]
			sentence.append(each_sentence)
		sentence_array.append(sentence)
	for i in range(len(content_array)):
		print('***************' + title_array[i] + '******************')
		print(content_array[i])

getUrl(path_array, title_array)
getContent(path_array, content_array, sentence_array)

for i in range(len(content_array)):
	print('***************' + title_array[i] + '******************')
	tokenized_contents = kkma.pos(content_array[i])
	noun_token = []
	for j in range(len(tokenized_contents)):
		if (tokenized_contents[j][1] == 'NNG') or (tokenized_contents[j][1] == 'NNP'):
			noun_token.append(tokenized_contents[j])

	cnt = Counter(noun_token)
	pprint(cnt.most_common(10))
	print('\n')