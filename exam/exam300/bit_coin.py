# -*- coding:UTF-8 -*-
import requests
"""
120
아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.


btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다.
최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장",
그렇지 않은 경우 "하락장" 문자열을 출력하라.


Key Name	Description
opening_price	최근 24시간 내 시작 거래금액
closing_price	최근 24시간 내 마지막 거래금액
min_price	최근 24시간 내 최저 거래금액
max_price	최근 24시간 내 최고 거래금액
"""
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

def viewStcok(dic) -> str :
    std = int(dic['opening_price']) + (int(dic['max_price']) - int(dic['min_price']))
    if int(dic['max_price']) > std :
        return '상승장'
    else :
        return '하락장'

print(viewStcok(btc))

