import re

p = re.compile('^https\:\/\/(\w+)\.(\w+)\.(\w+)')

url = 'https://www.daum.net'
result = p.search(url)

if result:
    print(len(result.groups()))
    print(result.groups(1))

r1 = re.search(r'\@...\|', '@abc|')

if r1:
    print(r1.group())

html_tag = "<a href='https://www.daum.net'>go daum</a>"

r2 = re.search(r'<.*?>', html_tag)

if r2:
    print(r2.group())

ahref = "https://www.python.org/about/"

rr = re.search(r'^http[s]?://', ahref);

if rr:
    print("success")

text = "Love wins. (always wins) - Morrie"

# (?<=\() 괄호 ( 을 시작으로 (?=\)) 마지막 괄호 ) 까지를 검색한다.
r3 = re.search(r'(?<=\()(.*?)(?=\))', text)

if r3:
    print(r3.group())

tt = "test-test"    

# r4 = re.

