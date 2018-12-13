# -*- coding: utf-8 -*-
x = 0

if x >= 1 :
    print("more than 1")
else :
    print("else!")
    
coffee = 10
money = 300
while money :
    coffee = coffee -1
    print("coffee sold")
    print("amount of leave coffee is " , coffee)
    if not coffee :
        print("out of coffee!!")
        break
    