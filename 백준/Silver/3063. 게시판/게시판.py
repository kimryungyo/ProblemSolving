from sys import stdin
I=stdin.readline
T=int(I())
for _ in range(T):
 a,b,c,d,e,f,g,h=map(int,I().split())
 p=(c-a)*(d-b)
 l=max(a,e)
 r=min(c,g)
 b=max(b,f)
 t=min(d,h)
 i=(r-l)*(t-b) if l<r and b<t else 0
 s=p-i
 print(s)
