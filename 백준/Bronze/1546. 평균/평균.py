N,*Q=map(int,open(0).read().split())
M=max(Q)
print(sum(n/M*100 for n in Q)/N)