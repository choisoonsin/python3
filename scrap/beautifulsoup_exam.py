# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 웹페이지 수신
html = urlopen("https://www.python.org/about")
# BeautifulSoup 객체로 변환
bsObject = BeautifulSoup(html, "html.parser")

# 전체 html 구조 
# print(bsObject.prettify())

# header
# print(bsObject.head)

# header > metas
for meta in bsObject.head.find_all("meta"):
    print(meta, "\t", meta.get("content"))

print("\r\n")

# header 안의 meta 태그중 name 속성(attribute) 값이 description인 대상 추출
tagForvalueIsDesciprtion = bsObject.head.find("meta", {"name":"description"})
print("속성 name의 값이 description인 대상 추출", tagForvalueIsDesciprtion, "What type is it?", type(tagForvalueIsDesciprtion))

print("\r\n")

print(tagForvalueIsDesciprtion.get("content"))

print("\r\n")

# 모든 링크의 텍스트와 주소 가져오기
linkList = []
for link in bsObject.find_all('a'):
    ahref = link.get("href")
    if re.search(r'^http[s]?://', ahref):
        linkList.append((link.text.strip(), link.get("href")))

print("linkList length is %d, data=\n%s" % (len(linkList),  linkList))

print("\r\n")

# select - list 반환
print(bsObject.select("span"))
