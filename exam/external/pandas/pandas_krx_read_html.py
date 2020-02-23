# -*- coding: utf-8 -*-
import os
import pandas as pd

def read_file():
    if os.access("./corpList.pkl", os.R_OK):
        return pd.read_pickle("./corpList.pkl")

df = read_file()
if df.empty == True: 
    df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]
    if len(df) > 0:
        df.to_pickle("./corpList.pkl")
else:
    print('pkl file was already created')
      
# rename columns      
df = df.rename(columns={'회사명':'name', '종목코드':'code'})
df = df[['name', 'code']]
df = df.set_index('code')
# print(df[df['name'].str.contains(r"모바일(?!$)")])

# convert dataframe to series
# You need to execute T to pivot dataframe before using iloc, because the df(dataframe) is vertical data
sr = df.T.iloc[0]
print(type(sr))