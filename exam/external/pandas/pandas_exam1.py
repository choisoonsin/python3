# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# Series 기초 - pandas 의 자료구조
print(pd.Series)

# 카카오 5일 종가
kakao = pd.Series([95000, 95600, 96422, 97000, 96500])

print(kakao)
print("\n")

# index 를 날짜로 설정
kakao2 = pd.Series([95000, 95600, 96422, 97000, 96500], index=[ "2019-01-05", 
                                                                "2019-01-06", 
                                                                "2019-01-07", 
                                                                "2019-01-08", 
                                                                "2019-01-09"]
                  )

print(kakao2)
print("\n")

# index 로 값 추출
print("2019-01-08 종가 추출", kakao2["2019-01-08"])

print(np.arange("2019-01-05", "2019-01-10", dtype='datetime64[D]'))

# To set datetime using numpy for index
# kakao3 = pd.Series([95000, 95600, 96422, 97000, 96500], index=np.tim)