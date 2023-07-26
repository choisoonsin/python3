# -*- coding: utf-8 -*-

import sys
from bs4 import BeautifulSoup
import requests

dart_url = "http://dart.fss.or.kr/dsae001/main.do"
krx_url = "http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx"

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

senddata1 = {
    "isuCd": "",	
    "no":	"P1",
    "mktsel":	"ALL",
    "searchText":	"모바일리더",
    "pagePath":	"/contents/COM/FinderStkIsu.jsp"
}

x = requests.post(krx_url, data=senddata1)
if x:
    bs = BeautifulSoup(x.text, "html.parser")
    print(bs.prettify())

