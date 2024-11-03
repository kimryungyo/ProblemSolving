A=list(map(abs,map(int,open(0).read().split())))
print(sum(A[1:A[0]+1])*2)