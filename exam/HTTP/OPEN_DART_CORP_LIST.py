from urllib.request import urlopen # HTTP 요청처리
from zipfile import ZipFile        # 공시회사정보 zipfile 처리
from io import BytesIO             # stream 데이터를 메모리에 적재
import os                          # 현재 디렉토리 정보를 얻기 위해
import xmltodict                   # xml을 dict로 파싱
from pathlib import Path           # file 존재유무 체크 유틸
import re 

def bind_params(params : dict):
    url_params = []
    for key in params:
        url_params.append(key + '=' + params[key])
    return url_params

def has_corpfile():
    dirpath = os.getcwd()

    if Path(dirpath + '\CORPCODE.xml').is_file():
        return True
    else:
        return False

    # 파일존재 체크 다른 방법들..
    # if os.path.isfile(dirpath + '\CORPCODE.xml'):
	#     return True
    # else:
    #     return False
    # try:
    #     open(dirpath + '\CORPCODE.xml', 'r')
    #     return True
    # except FileNotFoundError:
    #     return False

def get_corp_xml(url, params):

    if has_corpfile():
        dirpath = os.getcwd()
        return open(dirpath + '\CORPCODE.xml', 'r').read()
    else:
        url = url + '&'.join(bind_params(params))
        resp = urlopen(url)

        # zip으로 저장할경우
        # f = open( 'corpCode.zip', 'wb' )
        # f.write(resp.read())
        # f.close()

        # zip파일내용을 풀어 저장한다.
        zipfile = ZipFile(BytesIO(resp.read()))
        print(zipfile.namelist())
        for name in zipfile.namelist():
            z = zipfile.open(name)  
            with open(name, 'w') as codefile:
                for l in z.readlines():
                    codefile.write(l.decode()) 
        dirpath = os.getcwd()
        return open(dirpath + '\CORPCODE.xml', 'r').read()

""" Biz Start """

url = 'https://opendart.fss.or.kr/api/corpCode.xml?'
params = {
  'crtfc_key':'cert', # API 인증키
}

corp_dict = xmltodict.parse(get_corp_xml(url, params))

corp_list = corp_dict['result']['list']

corp_list_has_stockcode = [x for x in corp_list if x['stock_code'] is not None]

while(True):
    data_keyin = input('회사명을 입력하세요(종료하려면 exit 입력):')

    p = re.compile(r'.*({}).*'.format(data_keyin), re.IGNORECASE)

    if data_keyin == 'exit':
        break

    print('{}을 검색한 결과는 아래와 같습니다.'.format(data_keyin))
    print('=' * 100)

    for x in corp_list_has_stockcode:
        data = re.search(p, x['corp_name'])

        if data:
            result = data.group()
            print('회사명:{}, 고유코드:{}, 종목코드:{}'.format(result, x['corp_code'], x['stock_code']))

    print('=' * 100)
    

