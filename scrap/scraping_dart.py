# -*- coding: utf-8 -*-
"""
http://dart.fss.or.kr/ 사이트에서 기업개황 정보 스크래핑
"""
from bs4 import BeautifulSoup
import requests

dart_url = "http://dart.fss.or.kr/dsae001/main.do"

senddata = {
    "startDate":"",	
    "endDate":"",	
    "currentPage":"1",
    "maxResults":"45",
    "maxLinks":"10",
    "sort":"",	
    "series":"",	
    "selectKey":"",	
    "searchIndex":"",	
    "textCrpCik":"",	
    "autoSearch":"true",
    "textCrpNm":"모바일리더",
    "typesOfBusiness":"all",
    "corporationType":"all"
}

x = requests.post(dart_url, data=senddata)
if x:
    bs = BeautifulSoup(x.text, "html.parser")
    print(bs.prettify())

