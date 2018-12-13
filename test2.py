# searching for prime number
for n in range(2, 10):
    print('range1' , n)
    for x in range(2, n):
        print('range2' , x)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
            
def testMethod():
    pass                                
                
class Test:
    pass

