a=input("Enter string:")
c=0
a1=a[::-1]
for i in a1:
    if i!=" ":
        c+=1
    else:
        break
print(c)
