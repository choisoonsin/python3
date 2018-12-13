# -*- coding: utf-8 -*-
'''
    filter(function name , iterable param)
    : filter란 무엇인가를 걸러낸다는 뜻으로, filter 함수도 동일한 의미를 가진다. 
'''
from random import sample
print("_________________filter TEST_________________")
def positive(x):
    result = []
    for i in x :        
        if i > 0 :
            result.append(i)
    return result

sampleList = [1,2,-2,5,-5,-9]

# 일반적인 예
print(positive(sampleList))

def positiveForFilter(x):
    return x > 0; 

# filter 의 사용
print(list(filter(positiveForFilter , sampleList)))

# lambda 사용
print(list(filter(lambda x : x > 0 , sampleList)))    
    
'''
    hex(number)
    : 10진수를 16진수로 리턴
'''
print("_________________hex TEST_________________")
print(hex(9))
print(hex(10))
print(hex(15))

'''
    id(object)
    : 객체의 고유 주소값 리턴
'''
print("_________________id TEST_________________")
print(id(sampleList))

'''
    isinstance(object , class)
    : 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 리턴한다.
'''
print("_________________isinstance TEST_________________")
    
class Person : pass
class Company : pass

a = Person()
print(isinstance(a, Person))    # a instance 는 Person의 instance 이다.
print(isinstance(a, Company))

'''
    list(x)
    : list(s)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 리턴하는 함수이다.
'''
print("_________________list TEST_________________")
print(list('python'))
print(list(('python' , 'test')))
print(list({'name':'Peter','address':'USA'}))

'''
    map(iterable param)
    : map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. 
    map은 입력받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴하는 함수이다.
'''
print("_________________map TEST_________________")

def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

def two_timesForMap(x):
    return x * 2

print(list(map(two_timesForMap , [1,2,3,4])))

# lambda 사용
print(list(map(lambda x : x * 2 , [1,2,3,4])))
    