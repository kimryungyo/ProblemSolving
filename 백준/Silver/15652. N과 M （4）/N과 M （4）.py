N,M=map(int,input().split())
def recursion(s,N,M,l=1):
 if len(s)==M:print(" ".join(map(str, s)))
 else:
  for num in range(l,N+1):recursion(s+(num,),N,M,num)
recursion(tuple(), N, M)