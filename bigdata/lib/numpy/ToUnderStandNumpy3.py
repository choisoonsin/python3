# -*- coding : UTF-8 -*-
import numpy as np

x = np.array([1,2])
print(x.dtype)

x = np.array([1.0,2.0])
print(x.dtype)

x = np.array([1,2 , 3.0] , dtype=np.int64) # 3.0 의 경우 int형으로 파싱 된다.
print(x.dtype , x)


"""
배열 연산
기본적인 수학함수는 배열의 각 요소별로 동작하며 연산자를 통해 동작하거나 numpy 함수모듈을 통해 동작합니다:
"""
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

print("배열연산 x + y\n" , x+y) # or np.add(x , y)

print("배열연산 x - y\n" , x-y) # or np.subtract(x , y)

print("배열연산 x * y\n" , x*y) # or np.multiply(x , y)

print("배열연산 x / y\n" , x/y) # or np.divide(x , y)

print("배열연산 요소별 제곱근 np.sqrt(x) \n" , np.sqrt(x))