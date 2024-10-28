def S(n):
 l,r=0,n
 while l <= r:
  m=(l+r)//2
  if m*m>=n:r=m-1
  else:l=m+1
 return l
print(S(int(input())))