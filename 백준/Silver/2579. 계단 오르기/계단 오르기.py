import sys;s=lambda: int(sys.stdin.readline().rstrip());n=s();p=[s() for _ in range(n)];d=[0]*n;d[0]=p[0]
if n>1:d[1]=p[0]+p[1]
for i in range(2, n):d[i]=max(d[i-2]+p[i],d[i-3]+p[i-1]+p[i])
print(d[n-1])