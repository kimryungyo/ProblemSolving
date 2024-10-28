N,M=map(int,input().split())
print((pow(M,N)-pow(M-1,N))%(10**9+7))