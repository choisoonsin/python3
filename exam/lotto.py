import random

def get_lotto(manual_lotto=[]):
    if len(manual_lotto) == 6:
        return manual_lotto
    
    lotto = []
    while(len(lotto) <= 6):
        lotto.append(random.randrange(1 , 45))
        lotto = list(set(lotto))

    # lotto.sort(reverse=True)
    lotto.sort()
    return lotto

print("auto:", get_lotto())

print("manual", get_lotto([1,3,5,7,9,10]))
 
while(True):
    prom = input("Please insert key\nexit or lotto count you want\n:")
    if prom == "exit":
        break
    
    if prom.isdigit():
        x = 1
        while(x <= int(prom)):
            x += 1
            print(get_lotto())

 
    



