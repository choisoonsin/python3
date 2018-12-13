# -*- coding: utf-8 -*-
import json

data = {"name":"cyh" , "addr":"seoul" , "list":[{"a":"41"},{"b":"22"}] , "desc":"한국"}

d = json.dumps(data , indent=2)
print("desc:" , data.get("desc"))
print(d)
print(type(d))

print(type(data.get("name")) is list)
print(type(data.get("name")) is str)

print(isinstance(data.get("name") , list))
print(isinstance(data.get("name") , str))

r = json.loads(d)

print("______________")
print(type(r))

