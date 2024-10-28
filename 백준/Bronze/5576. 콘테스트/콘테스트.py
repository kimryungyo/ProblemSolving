Q=list(map(int,open(0).read().split()))
X,Y=Q[:10],Q[10:]
s,r=sum,sorted
print(s(r(X)[-3:]),s(r(Y)[-3:]))