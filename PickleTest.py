# -*- coding: utf-8 -*-
import pickle

f = open("C:\\test.txt" , 'wb')

data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

pickle.dump(data , f)

f.close()
