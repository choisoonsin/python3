import re

_target_string = """copyNode("/root/src[" + row + "]/item", "/root/dest[" + row + "]/item")"""

_pattern = re.compile(r'copyNode\(([^,]*)[,+\s+]([^)]*)\)+;?')

_r = re.search(_pattern, _target_string)

print(_r.groups())
data = '삼성전자'

list = ['삼성전자', 'LG전자', '삼성엔지니어링', 'LG화학']

# data_keyin = input()
data_keyin = 'lg'

for x in list:
    data = re.search(r'.*({}).*'.format(data_keyin), x, re.I)

    if data:
        result = data.group()
        print(result)
