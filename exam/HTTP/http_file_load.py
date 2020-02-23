from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO

url = "https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key=781ecb967f28dd7f8fff290ded1e5365426990df"

resp = urlopen(url)

with ZipFile(BytesIO(resp.read())) as zf:
  file_list = zf.namelist()
  while len(file_list) > 0:
    file_name = file_list.pop()
    print(file_name)