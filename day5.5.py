a=int(input("Enter list of elements:"))
c=[]
d=[]
for i in range(a):
    b=int(input("Enter element:"))
    c.append(b)
d=c.copy()
print("INPUT=",d)
c.sort()
for i in range(0,a):
    if(c[a-1]==d[i]):
        f=i
print("OUTPUT=",f)
