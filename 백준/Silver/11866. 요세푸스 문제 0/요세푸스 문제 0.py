N,M=map(int,input().split())
l=[n for n in range(1,N+1)]
a=[]
r=M-1
while l:
 v=l.pop(r);a.append(str(v))
 if l:r+=M-1;r%=len(l)
print(f"<{', '.join(a)}>")