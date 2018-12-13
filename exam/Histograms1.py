'''
Created on 2018. 11. 7.

@author: THEK
'''
a = (1 , 1 , 3 , 4 , 5 , 5 , 7 , 7 , 23 , 1 , 3)

def count_element(seq) -> dict:
    hist = {}
    for i in seq :
        hist[i] = hist.get(i, 0) + 1
    return hist

counted = count_element(a)
print(counted)

from collections import Counter

recounted = Counter(a)
print(type(recounted))
print(recounted.items())
print(counted.items())

b = (51 , 99)
recounted.update(b)
# recounted = Counter(b)
print(recounted)

c = "This is Test Module"
d = list(c)

dCounted = Counter(d)
print(dCounted)