from collections import Counter

phrase = "a man a plan a canal panama"

print(type(phrase.split()))

cntr = Counter(phrase.split())
print(cntr.most_common())

