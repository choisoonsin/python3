# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 웹페이지 수신
html = urlopen("https://www.python.org/about")
# BeautifulSoup 객체로 변환
bsObject = BeautifulSoup(html, "html.parser")

# 전체 html 구조 
test_html_string = bsObject.prettify()

# Using open Built-in functions to write html tag
html_file_name = "C:\\html.txt"
with open(html_file_name, mode='r', encoding='utf8') as f:
    read_data = f.read()
    print(len(read_data))
    if read_data:
        print("passed")
    else:
        with open(html_file_name, mode='w', encoding='utf8') as f:
            f.write(test_html_string)

# header
# print(bsObject.head)

# header > metas
for meta in bsObject.head.find_all("meta"):
    print(meta, "\t", meta.get("content"))

print("\r\n")

# header 안의 meta 태그중 name 속성(attribute) 값이 description인 대상 추출
tags_that_has_desciprtion = bsObject.head.find("meta", {"name":"description"})
print("속성 name의 값이 description인 대상 추출", tags_that_has_desciprtion, "What type is it?", type(tags_that_has_desciprtion))

print("\r\n")

print(tags_that_has_desciprtion.get("content"))

print("\r\n")

# 모든 링크의 텍스트와 주소 가져오기
linkList = []
for link in bsObject.find_all('a'):
    ahref = link.get("href")
    if re.search(r'^http[s]?://', ahref):
        linkList.append((link.text.strip(), link.get("href")))

print("linkList length is %d, data=\n%s" % (len(linkList),  linkList))

print("\r\n")


""" CSS Selector """
# body내에 div 중 id가 nojs 인 tag 선택
tags_nojs = bsObject.select("body > div > #nojs")

if tags_nojs:
    for tag in tags_nojs:
        print(tag)

# 첫번째 menu class를 갖는 ul태그의 출력
tags_menu = bsObject.select_one("ul.menu")

print(tags_menu)