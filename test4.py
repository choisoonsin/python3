def append(a , L=[]):
    L.append(a)
    return L        

print(append('a'))
print(append('b'))
print(append('c'))

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print(voltage , state , action , type)
    
parrot('a' , 'b' , 'c')

parrot(voltage=10 , action='b' , type='c')

parrot(50 , action='b' , type='c')    