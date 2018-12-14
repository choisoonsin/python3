# -*- coding : UTF-8 -*-
import numpy as np

a = np.array([1,2,3]) # rank 가 1인 배열 생성
print(type(a))
print(a.shape)

b = np.array([[1,2,3] , [4,5,6]]) # rank 가 2 인 배열 생성 행:2 , 열:3
print(b.shape)

l = [1,1,1]
print(l)

zero = np.zeros((2,2))
print("zero:\n" , zero)

zero = np.zeros((4,3))
print("zero:\n" , zero)

one = np.ones((2,2))
print("one:\n" , one)
print(type(one[1][1])) # ones 로 생성하면 numpy.float64 자료형태를 가진다.

full = np.full((2,4) , 3) # 모든 값이 특정 상수값을 가지는 배열 생성
print("full:\n" , full)
print(full[0][3])

eye = np.eye(5) # 5x5 대각행렬
print("eye:\n" , eye)

rand = np.random.random((2,2))
print("rand:\n" , rand)

"""
배열 인덱싱

Numpy는 배열을 인덱싱하는 몇 가지 방법을 제공합니다.

슬라이싱: 파이썬 리스트와 유사하게, Numpy 배열도 슬라이싱이 가능합니다. 
Numpy 배열은 다차원인 경우가 많기에, 각 차원별로 어떻게 슬라이스할건지 명확히 해야 합니다:
"""
exam1 = np.array([[1,2,3,4] , [5,6,7,8] , [9,10,11,12]])

"""
슬라이싱을 이용하여 첫 두 행과 1열, 2열로 이루어진 부분배열을 만들어 봅시다;
b는 shape가 (2,2)인 배열이 됩니다:
"""
slice1 = exam1[:2 , :2]
print("slice1\n" , slice1)

slice2 = exam1[: , 1::2]
print("slice2\n" , slice2)

""" 슬라이싱 된 배열은 원본 배열과 같은 데이터를 참조함."""
print(exam1[0,1])
slice1[0,1] = 77        # 슬라이싱 된 배열 수정.
print(exam1[0,1])       # 원본데이터 수정 확인.

"""
정수 배열 인덱싱: Numpy 배열을 슬라이싱하면, 결과로 얻어지는 배열은 언제나 원본 배열의 부분 배열입니다. 
그러나 정수 배열 인덱싱을 한다면, 원본과 다른 배열을 만들 수 있습니다. 여기에 예시가 있습니다:
"""
exam2 = np.array([[1,2], [3, 4], [5, 6]])
print(exam2[[0,1,0] , [0,1,1]])
idx = 0;
exam3 = np.array([[1,2,3] , [4,5,6] , [7,8,9] , [10,11,12]])
print("exam3\n" , exam3)

b = np.array([0, 2, 0, 1])
print("b\n" , b , b.shape)

print("np.arange:\n" , np.arange(4))

"""
b 에 저장된 인덱스를 이용해 각 행에서 하나의 요소를 선택합니다.
"""
print("exam3 array\n" , exam3[np.arange(4) , b])

"""
b 에 저장된 인덱스를 이용해 각 행에서 하나의 요소를 변경합니다.
"""
exam3[np.arange(4) , b] += 10

print("Added exam3 array\n" , exam3)



"""

불리언 배열 인덱싱: 불리언 배열 인덱싱을 통해 배열 속 요소를 취사선택할 수 있습니다. 
불리언 배열 인덱싱은 특정 조건을 만족하게 하는 요소만 선택하고자 할 때 자주 사용됩니다. 
다음은 그 예시입니다:

"""
exam4 = np.array([[1,2] , [3,4] , [5,6]])

bool_idx = (exam4 > 2) # 2 보다 큰 exam4 의 요소를 찾는다.

# 이 코드는 exam4 와 shape가 같고 불리언 자료형을 요소로 하는 numpy 배열을 반환함

print("bool_idx\n" , bool_idx)

# bool_idx 를 사용하여 참 값을 가지는 요소로 구성되는 rank1 인 배열을 구성 할 수 있다.

print("exam4[bool_idx]\n" , exam4[bool_idx])

# 위 과정을 아래 한 문장으로 처리 할 수 있다.

print("exam4[exam4 > 2]\n" , exam4[exam4 > 2])