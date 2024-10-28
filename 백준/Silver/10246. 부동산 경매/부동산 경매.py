m=10**6+1;c=[0]*m;s=0;d=[0]*m
for K in range(1,m):s+=K+1;c[K]=s
for i in range(m):
 for j in range(i,m):
  k=c[j]-c[i]
  if k>1e6:break
  d[k]+=1
for v in open(0).read().split()[:-1]:print(d[int(v)])