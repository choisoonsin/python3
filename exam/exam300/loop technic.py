# -*- condig : UTF-8 -*-

animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)

""" 만약 반복문 내에서 리스트 각 요소의 인덱스에 접근하고 싶다면, ‘enumerate’ 함수를 사용하세요: """

for idx , animal in enumerate(animals) :
    print(idx , ":" , animal)


"""
리스트 comprehensions: 프로그래밍을 하다 보면, 자료형을 변환해야 하는 경우가 자주 있습니다. 
간단한 예를 들자면, 숫자의 제곱을 계산하는 다음의 코드를 보세요:
"""
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)
"""
리스트 comprehension을 이용해 이 코드를 더 간단하게 만들 수 있습니다:
"""
squares = [x ** 2 for x in nums ]
print(squares)

"""
리스트 comprehensions에 조건을 추가할 수도 있습니다:
"""
squares = [x ** 2 for x in nums if x % 2 == 0]
print(squares)

print("=" * 100)

