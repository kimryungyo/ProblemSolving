from sys import stdin;s=stdin.readline
N,M=map(int,s().split());g=[s()[:-1]for _ in' '*N];w=[]
c=[[0]*M for _ in' '*N]
for y in range(N):
 for x in range(M):
  if g[y][x]=='+'and not c[y][x]:
   n=x;i=0
   while 1:
    n+=1
    if g[y][n]=='+':break
    elif g[y][n]=='|':
     if not i:i=n
     else:m=g[y][i+1:n]
   j=y
   while 1:
    j+=1
    if g[j][n]=='+':break
   for v in[y,j]:
    for u in[x,n]:c[v][u]=1
   w+=[(m,y,x,j,n)]
w.sort(key=lambda x:x[0])
r=[['.']* M for _ in' '*N];p=0
for m,a,b,d,e in w:
 for y in range(a,d+1):
  for x in range(b,e+1):r[p+y-a][p+x-b]=g[y][x]
 p+=1
for l in r:print(''.join(l))