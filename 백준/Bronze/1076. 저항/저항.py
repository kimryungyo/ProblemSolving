a,b,c=[[4,0,6,2,3,8,7,1,9,5].index(sum(map(ord,v))*15%203%10) for v in open(0).read().split()]
print((a*10+b)*10**c)