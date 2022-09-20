n = []
maxi = 0

while True:
  s = input()
  if s == '*':
    break
  else:
    n.append(s)

for i in n:
  s = i.split()
  maxi = max(maxi,len(s))

print(maxi)
