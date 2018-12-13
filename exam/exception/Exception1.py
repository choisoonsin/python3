# -*- coding: utf-8 -*-
try:
    f = open("c:\\testError.txt" , 'r')
    i = 4/0
except FileNotFoundError as e:
    print(e)    
except ZeroDivisionError :
    print(":) ZeroDivisionError , division by zero")
'''
    you can also express one more exceptions
    except (FileNotFoundError , ZeroDivisionError) as e:
'''    
try :    
    i = [1,2,3]
    print(i[4])
except IndexError as e:
    print(e)
    
    
'''
    try else expression
'''
try : 
    f = open("c:\\test.txt" , 'r')
except :
    print("File not found Exception: No such directory or file")
else :
    print(type(f))
    print(f.readline())
finally:
    print("Execute finally")
    f.close()    
        
            



