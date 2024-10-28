d=10**9+7
q={1:1,2:1,3:2,4:3,5:5}
def p(n):
 if n not in q:q[n]=(p(n//2)**2+p(n//2+1)**2)%d if n%2==1 else(p(n+1)-p(n-1))%d
 return q[n]
print(p(int(input())))