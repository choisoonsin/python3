from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
import os

def bind_params(params : dict):
  url_params = []
  for key in params:
    url_params.append(key + '=' + params[key])
  return url_params

def has_corpfile():
  dirpath = os.getcwd()
  try:
    corpfile = open(dirpath + '\CORPCODE.xml', 'r')
    return True
  except FileNotFoundError:
    return False
  

url = 'https://opendart.fss.or.kr/api/corpCode.xml?'
params = {
  'crtfc_key':'781ecb967f28dd7f8fff290ded1e5365426990df', # API 인증키
}

if has_corpfile():
  dirpath = os.getcwd()
  corp_data = open(dirpath + '\CORPCODE.xml', 'r').read()
  print(corp_data)
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