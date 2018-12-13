# -*- coding: utf-8 -*-
import pickle

f = open("C:\\test.txt" , 'rb')

load = pickle.load(f)

print(load)

f.close()
