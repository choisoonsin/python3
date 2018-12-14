# -*- coding:UTF-8 -*-
"""
051
price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
출력 예시:
[100, 130, 140, 150, 160, 170]
"""
price = ['20180728', 100, 130, 140, 150, 160, 170]

print("051:" , price[1:])

"""
052
슬라이싱을 사용해서 홀수만 출력하라.

실행 예:
[1, 3, 5, 7, 9]
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("052:" , nums[::2]) # +2 index 서치 0 , 0+2 , 2+2 , 4+2 = 0 , 2 , 4 , 6


"""
053
슬라이싱을 사용해서 짝수만 출력하라.
"""
print("052:" , nums[1::2]) # nums[1::2] 의 경우 index 1 부터 시작

"""
054
슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.

실행 예:
[5, 4, 3, 2, 1]
"""
nums = [1, 2, 3, 4, 5]

print("054:" , nums[5::-1])

"""
055
interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest 리스트를 사용하여 아래와 같이 화면에 출력하라.

출력 예시:
삼성전자 Naver
"""
interest = ['삼성전자', 'LG전자', 'Naver']

print("055:" , interest[0]+interest[2])

"""
056
interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest 리스트를 사용하여 아래와 같이 화면에 출력하라.

출력 예시:
삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
"""
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

# s = "";
# for d in interest :
#     s += ' '+d

print("056:" , ' '.join(interest))

"""
057
interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest 리스트를 사용하여 아래와 같이 화면에 출력하라.

출력 예시:
삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
"""
print("057:" , '/'.join(interest))

"""
058
interest 리스트에는 아래의 데이터가 바인딩되어 있다.
join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.

출력 예시:
삼성전자
LG전자
Naver
SK하이닉스
미래에셋대우
"""
print("058:" , '\n'.join(interest))

"""
059
회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
이를 interest 이름의 리스트로 분리 저장하라.

실행 예시
>> print(interest)
['삼성전자', 'LG전자', 'Naver']
"""
s = "삼성전자/LG전자/Naver"
sList = s.split("/")
print("059: " , sList , type(sList))

"""
060
회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
이를 interest 이름의 리스트로 분리 저장하라.

실행 예시
>> print(interest)
['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
"""
s = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
sList = s.split("/")
print("060: " , sList , type(sList))