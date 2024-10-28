n=int(input())
if n<100:c=n
else:
 c=99
 for a in range(100,n+1):
  b=list(map(int,str(a)))
  if b[0]-b[1]==b[1]-b[2]:c+=1
print(c)