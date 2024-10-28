N=int(input())
P=[0]*N
for _ in range(N*(N-1)//2):
 A,B,C,D=map(int,input().split())
 if C>D:P[A-1]+=3
 elif C<D:P[B-1]+=3
 else:P[A-1]+=1;P[B-1]+=1
for i in range(N):
 r=1
 for j in range(N):
  if P[j]>P[i]:r+=1
 print(r)