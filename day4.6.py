a=input("enter the string:")
b=input("enter a character to be deleted:")
c=len(a)
d=""
for i in range(0,c):
  if a[i] not in b:
    d+=a[i]
print("string after the character is removed:",d)
