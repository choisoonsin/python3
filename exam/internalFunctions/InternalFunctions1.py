# -*- coding: utf-8 -*-

'''
    abs(absolute value)
'''
print(abs(-5))
print(abs(5))

'''
    all(x)
    x must be iterable , if all of them is true , it returns true
'''
trueList = [1,2,3,4,5]
print("trueList:" , all(trueList))

falseList1 = [1,2,3,0,5]
falseList2 = ['a' , 'b' , '' , 'd']
print("falseList1:" , all(falseList1))      
print("falseList2:" , all(falseList2))

trueTuple = (1,2,3)
print("trueTuple:" , all(trueTuple))      

''' 
    any(x)
    opposition of all(x) 하나라도 True 값이 있으면 True 리턴
'''
anyList = [1,2,3,0]
print("anyList:" , any(anyList))    

'''
    chr(asciiCode)
'''
print(chr(97))

'''
    dir(object)
    : 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다. 아래 예는 리스트와 딕셔너리 객체의 관련 함수들(메서드)을 보여 주는 예이다.
'''    
print("_________________DIR TEST_________________")
# List 형
print(dir([1,2,3]))

# Tuple 형
print(dir((1,2,3)))

'''
    divmod(x, y)
    : 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 리턴하는 함수이다.
'''
print("_________________DIVMOD TEST_________________")
print(divmod(20, 3))
print("x//y" , divmod(20, 3)[0])
print("x%y" , divmod(20, 3)[1])   

'''
    enumerate
    : 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
'''
print("_________________enumerate TEST_________________")
listForEnum = ['head' , 'body' , 'foo' , 'bar']
enumed = enumerate(listForEnum)
print("enumed:" , enumed)
# for x in enumed :
#     print(type(x))
#     print(x)
    
for idx , value in enumed :
    print(idx , value)    
    
'''
    eval(expression)
    : eval(expression)은 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을 입력으로 받아 문자열을 실행한 결과값을 리턴하는 함수이다.
    : 보통 eval은 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶은 경우에 사용된다.
'''    
print("_________________eval TEST_________________")
print(eval('1+2'))
print(eval('divmod(10,4)'))
    