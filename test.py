# x = int(input("Please enter an integer \n"));
x = 100

print(x)

if x >= 90 :
    print("A")
elif x >=50 and x < 90 :
    print("B")
else :
    print("C")

words = ["apple" , "carrot" , "pear"]

for x in words :
    print("["+x+"] length : " , len(x))

# sequence of Number
for x in range(5) :
    print(x)

print (range(len(words)))
    
for i in range(len(words)) :
    print(i , words[i])
     
    