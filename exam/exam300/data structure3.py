# -*- coding:UTF-8 -*-
"""
071
기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다. 하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다. 튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.

>> a, b, *c = (0, 1, 2, 3, 4, 5)
>> a
0
>> b
1
>> c
[2, 3, 4]
다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.
"""
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

*valid_score , a , b = scores;
print("071:" , valid_score)

# 값을 사용할 필요가 없는 경우 _ (underscore) 사용
*valid_score , _ , _ = scores;

_ , _ , *valid_score = scores;
print("072:" , valid_score)

_ , *valid_score , _ = scores;
print("073:" , valid_score)

try:
    _ , _ , _ ,_ , _ , _ ,_ , _ , _ ,_ , _ , _ , *valid_score  = scores  # <<< error!!!
except ValueError as e :
    print("073-1:" , e)

"""
074
temp 이름의 비어있는 딕셔너리를 만들라.
"""
temp = {}
print("074:" , type(temp))

"""
075
다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.

이름	희망 가격
메로나	1000
폴라포	1200
빵빠레	1800
"""
temp = {'메로나':1000 , '폴라포':1200 , '빵빠레':1800}
print("075:" , temp)

"""
076
075 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.

이름	희망 가격
죠스바	1200
월드콘	1500
"""
temp['죠스바'] = 1200
temp['월드콘'] = 1500
print("076:" , temp)


"""
077
074에서 만든 딕셔너리를 사용하여 메로나 가격을 출력하라.

실행 예:
메로나 가격: 1000
"""
print("077: 메로나 가격:%d"%temp.get('메로나'))

"""
078
075에서 만든 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
"""
temp['메로나'] = 1300
print("078: 메로나 가격:%d"%temp.get('메로나'))

"""
079
076에서 만든 딕셔너리에 메로나를 삭제하라.
"""
del temp['메로나']
print("079" , temp)

"""
081
아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다.

이름	가격	재고
메로나	300	20
비비빅	400	3
죠스바	250	100
"""
iceList = {'메로나' : [300 , 20] , '비비빅' : [400,3] , '죠스바' : [250 , 100]}
print("081:" , iceList , type(iceList['메로나']))

"""
082
081의 inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.

실행 예시:
300 원
"""
print("082: 메로나 가격:%d" %iceList['메로나'][0])

"""
083
081의 inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.

실행 예시:
20 개
"""
print("083: 메로나 재고:%d" %iceList['메로나'][1])

"""
084
081의 inventory 딕셔너리에 아래 데이터를 추가하라.

이름	가격	재고
월드콘	500	7
"""
iceList['월드콘'] = [500,7]
print("084:" , iceList)

"""
085
다음의 딕셔너리에서 key 값으로만 구성된 리스트를 생성하라.
"""
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

iceKeys = list(icecream.keys())
print("085:" , iceKeys)


"""
087
icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
"""
print("087:" , sum(list(icecream.values())))

"""
088
아래의 new_product 딕셔너리를 087번의 icecream 딕셔너리에 추가하라.
"""
new_product = {'팥빙수':2700, '아맛나':1000}
new_list = [1,2,3,4,5]

icecream.update(new_product)
#icecream.update(new_list)    # TypeError : 딕셔너리 타입으로 변환 오류
print("088:" , icecream)


"""
089
아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.
"""
keys = ('apple', 'pear', 'peach')
vals = (300, 250, 400)

new_dict = dict(zip(keys , vals))       # zip 은 두개의 자료구조를 하나로 합쳐줌.
print("089:" , new_dict)
