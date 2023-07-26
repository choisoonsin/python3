# -*- coding : UTF-8 -*-
import numpy as np

x = np.array([1,2])
print(x.dtype)

x = np.array([1.0,2.0])
print(x.dtype)

x = np.array([1,2 , 3.0] , dtype=np.int64) # 3.0 의 경우 int형으로 파싱 된다.
print(x.dtype , x)