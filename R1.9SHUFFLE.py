def shuffle(l1,l2):
  c=[]
  if len(l1)!=0 and len(l2)!=0:
    for i in range(min(len(l1), len(l2))):
      c.extend([l1[i],l2[i]])      
    c.extend(l1[i+1:] or l2[i+1:])
  else:
    c.extend(l1[0:] or l2[0:])      
  return (c)

l = []
s2 = []
print("Enter element for l1: \n")
while True:
  s = input()
  if s == '*':
    break
  else:
    l.append(int(s))

print("Enter element for l2: \n")
while True:
  s = input()
  if s == '*':
    break
  else:
    s2.append(int(s))

print(shuffle(l,s2))

