# -*- coding: utf-8 -*-
import sys
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO

sys.path.append('C://users//cyh02//anaconda3//lib//site-packages ')
import pandas as pd
import json

print('path:', sys.path)

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

resp = urlopen(url)


if resp.code == 200:
    resp_json = resp.read().decode()
    resp_json = json.loads(resp_json)

    print(list(resp_json.items()))

    data = pd.json_normalize(resp_json)
    print(data.head())

#df.show()