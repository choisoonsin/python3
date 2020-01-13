import requests
import re
from bs4 import BeautifulSoup
from urllib import parse

url = "https://search.naver.com/search.naver"

def makeUrlForNaver(url, searchName):
    # encodeName = parse.quote(searchName)
    return url + "?where=news&sm=tab_jum&query=" + searchName

# ?q=SFA%EB%B0%98%EB%8F%84%EC%B2%B4&oq=SFA%EB%B0%98%EB%8F%84%EC%B2%B4"

urlMaked = makeUrlForNaver(url, "SFA반도체")

# print(urlMaked)

r = requests.get(urlMaked)

"""
<a href="http://nbntv.co.kr/news/view/784477" target="_blank" class="_sp_each_url _sp_each_title" onclick="return goOtherCR(this, 'a=nws*b.tit&r=17&i=8817ca61_000000000000000000674053&g=5544.0000674053&u='+urlencode(this.href));" title="SFA반도체실시간증시 24일 현재 3735원"><strong class="hl">SFA반도체</strong>실시간증시 24일 현재 3735원</a>
"""
if r.status_code == 200:
    print("success")

    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.prettify())

    print(soup.title)
else:
    print("failed")