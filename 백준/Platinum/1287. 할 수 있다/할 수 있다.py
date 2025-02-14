from re import sub
def q(r):
 b=c="";d=0 
 for e in r:
  if e=="(":d+=1
  elif e==")":d-=1
  if d>100:c+=e
  elif c:c+=")";b+=str(q(c));c=""
  else:b+=e
 return eval(b)
def n(z):return str(int(z.group()))
m=sub(r'\b0+(\d+)\b',n,input())
try:
 if "()" in m:raise 0
 l="".join("&" if h in {"+","-","*","/"} else h for h in m);q(l);print(q(m.replace("/","//")))
except:print("ROCK")