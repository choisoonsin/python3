from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
import Requests

def bind_params(params : dict):
  url_params = []
  for key in params:
    url_params.append(key + '=' + params[key])
  return url_params

url = 'https://opendart.fss.or.kr/api/company.json?'
params = {
  'crtfc_key':'781ecb967f28dd7f8fff290ded1e5365426990df', # API 인증키
  'corp_code':'00132008'
}

url = url + '&'.join(bind_params(params))

resp = urlopen('https://github.com')
print(resp.read())



# print(url)

# ssl.OPENSSL_VERSION
# resp = urlopen(url)

# print(resp)

# with ZipFile(BytesIO(resp.read())) as zf:
#   file_list = zf.namelist()
#   while len(file_list) > 0:
#     file_name = file_list.pop()
#     print(file_name)