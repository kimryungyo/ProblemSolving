import bisect;N,K,*q=map(int,open(0).read().split())
p=[];g=0
for i in range(N):
 bisect.insort_left(p,q[i]);l=len(p)
 if l>=K:
  if l>K:p.remove(q[i-K])
  g+=p[-~K//2-1]
print(g)