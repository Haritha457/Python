import math
a=int(input())
b=[]
if a>0:
    print("Factorial =",math.factorial(a))
    for i in range(1,a+1):
        if a%i==0:
            b.append(i)
    print("Number of factors :",len(b))
else:
    print("invalied input")
