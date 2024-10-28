N,M,K,*C=map(int,open(0).read().split())
print(min(range(K),key=lambda i:C[i*2]-C[i*2+1])+1)