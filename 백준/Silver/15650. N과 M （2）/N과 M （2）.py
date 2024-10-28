N,M=map(int,input().split())
def recursion(s,N,M,l=0):
 if len(s)==M:print(" ".join(map(str, s)))
 else:
  for num in range(l+1,N+1):recursion(s+(num,),N,M,num)
recursion(tuple(), N, M)