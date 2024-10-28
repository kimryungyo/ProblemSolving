a,b=map(int,input().split())
s=b*(b+1)/2
print(-1 if a<s else (b if (a-s)%b>0 else b-1))