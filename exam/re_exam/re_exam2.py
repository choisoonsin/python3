import re

data = '삼성전자'

list = ['삼성전자', 'LG전자', '삼성엔지니어링', 'LG화학']

# data_keyin = input()
data_keyin = 'lg'

for x in list:
    data = re.search(r'.*({}).*'.format(data_keyin), x, re.I)

    if data:
        result = data.group()
        print(result)
