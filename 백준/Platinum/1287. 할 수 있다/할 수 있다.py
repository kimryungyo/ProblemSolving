import re
def q(r):
 b=c='';d=0
 for e in r:
  if e=='(':d+=1
  elif e==')':d-=1
  if d>100:c+=e
  elif c:c+=')';b+=str(q(c));c=''
  else:b+=e
 return eval(b)
m=re.sub(r'\b0+(\d+)\b',lambda z:str(int(z.group())),input())
try:
 if'()'in m:raise
 q(''.join('&'if h in'+-*/'else h for h in m));print(q(m.replace('/','//')))
except:print("ROCK")
