import requests
from bs4 import BeautifulSoup as Soup
from selenium import webdriver
from konlpy.tag import Kkma

def getContent(path):
	url = path
	r = requests.get(url)
	if r.status_code == 200:
		soup = Soup(r.text, "html.parser")
		content_list = soup.find_all(class_='wrap_item item_type_text')
		tmp_content = ''
		for i in range(len(content_list)):
			tmp_content += content_list[i].get_text('data-app')

		content = tmp_content

	content = content.replace("data-app", "")
	print('***************' + path + '******************')
	print(content)

getContent("https://brunch.co.kr/@officen/15")