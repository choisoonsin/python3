# -*- coding: utf-8 -*-
class calculator:
    
    def __init__(self):
        print("Created calculator")
        self.a = 0
        self.b = 0
    
    def add(self , a , b):
        self.first = a
        self.second = b
        
    def minus(self , a , b):
        self.a = a
        self.b = b
            

class extendCal(calculator):
    pass
    
print(type(calculator))

x = 1

print(type(x))    
    
cal1 = calculator()
cal2 = calculator()
cal1.add(10,5)
cal2.add(7,3)
print(cal1.first) 

cal1.minus(100, 200)

print(cal1.a)
print(cal2.b)   

cal3 = extendCal()
