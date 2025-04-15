i={'A':(1,2),'B':(1,3),'C':(1,4),'D':(2,3),'E':(2,4),'F':(3,4)}
s,b=1,4
for p in input():
 a,c=i[p]
 s=c if s==a else a if s==c else s
 b=c if b==a else a if b==c else b
print(s)
print(b)