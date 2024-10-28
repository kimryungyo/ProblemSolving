import math;N,M=map(int,input().split());o=0
for i in range(M):
 c=(9-i)**N*math.comb(M,i+1)
 if i%2==0:c*=-1
 o-=c
print(10**N-o)