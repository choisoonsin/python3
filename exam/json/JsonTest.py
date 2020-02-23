# -*- coding: utf-8 -*-
import json

data = {
  "name":"Hong gil dong", 
  "addr":"seoul, Korea", 
  "age": 37,
  "hobbies":["Watching movie", "Reading Novels"],
}

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

