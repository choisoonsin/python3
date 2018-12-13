# -*- coding: utf-8 -*-
'''
    ord(character)
    :chr 의 반대
'''
from exam.internalFunctions.InternalFunctions2 import sampleList
print("_________________ord TEST_________________")

print(ord('a'))

'''
    pow(x,y)
'''
print("_________________pow TEST_________________")

print(pow(2,10))

'''
    range(x,y,z)
'''
print("_________________range TEST_________________")

print(list(range(5)))  

print(list(range(5,10)))  

print(list(range(1,10,2)))

print(list(range(10,1,-2)))

'''
    round(x,y)
'''
print("_________________round TEST_________________")

print(round(2.6))

print(round(3.1415942 , 2))

'''
    sorted(iterable, key=None, reverse=False)
'''
print("_________________sorted TEST_________________")

s = [3,1,5,2,3,1,6]

print(s.sort())
print(s)

# sort of list and sorted are different
ss = [3,1,5,2,3,1,6]
print(sorted(ss, key=None, reverse=True))

'''
    str(object)
'''
print("_________________str TEST_________________")

print(str(1)+'hi')

'''
    tuple(iterable) / set(iterable)
'''
print("_________________tuple TEST_________________")

print(tuple(ss))
print(set(ss))


