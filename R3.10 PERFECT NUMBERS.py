n=int(input("Enter the value of N : "))
count=0
a=1;
while count<=n:
    sum=0
    for b in range (1,(a//2)+1):
        if a%b==0:
            sum=sum+b
    if sum==a:
        print(a ,end=' ')
        count+=1
    a+=1
for i in range(1,a+1):
        if a%i==0:
            b.append(i)
print("Number of factors :",len(b))
