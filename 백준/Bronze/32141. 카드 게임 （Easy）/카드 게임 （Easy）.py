m=lambda:list(map(int,input().split()));N,H=m();d=m();t=0;v=-1
for i in range(N):
 t+=d[i]
 if t>=H:v=i+1;break
print(v)