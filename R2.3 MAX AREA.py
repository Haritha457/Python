def maxArea(A,Len):
    area=0
    for i in range (Len):
         for j in range (i+1,Len):
                  area =max(area,min(A[j],A[i])*(j-i))
    return area
a=int(input(" enter the numbers of elements :"))
if(a>0):
    b=[]
    for i in range (0,a):
        c=int(input(" enter the number:"))
        b.append(c)
print("INPUT ARRAY=",b)
print("OUTPUT=",maxArea(b,a))
        
