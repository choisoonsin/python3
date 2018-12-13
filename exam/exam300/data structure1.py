# -*- coding:UTF-8 -*-
"""
2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 리스트에 저장하라. (순위 정보는 저장하지 않는다.)

순위	영화
1	닥터 스트레인지
2	스플릿
3	럭키
"""

# 041
list = ['닥터 스트레인지' , '스플릿' , '럭키']

print("041:" , list , type(list))

"""
042
041의 movie_rank 리스트에 "배트맨"을 추가하라.
"""

# 042
list.append('배트맨')

print("042:" , list)

"""
043
movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
"""

# 043
list.insert(1 , '슈퍼맨')

print("043:" , list)

"""
044
movie_rank 리스트에서 '럭키'를 삭제하라.
"""

# 044
list.remove("럭키")
#del list[3]

print("044:" , list)

"""
045
movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
"""

list.remove("스플릿")
list.remove("배트맨")
#del list[2:]

print("045:" , list)


"""
046
lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
"""
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
"""
실행 예:
>> langs
['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']
"""

langs = lang1 + lang2

print("046:" , langs)

"""
047
다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
"""
nums = [1, 2, 3, 4, 5, 6, 7]
"""
실행 예:
max:  7
min:  1
"""

print("047:" , "max: %d , min %d" %(max(nums) , min(nums)))


"""
048
다음 리스트의 합을 출력하라.

실행 예:
15
"""
nums = [1, 2, 3, 4, 5]

print("048: sum=%d" %sum(nums))


"""
049
다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
"""
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]

print("049: count:%d" %len(cook))

"""
050
다음 리스트의 평균을 출력하라.

실행 예:
3.0
"""
nums = [1, 2, 3, 4, 5]

print("050: avg:%d" %(sum(nums) / len(nums)))