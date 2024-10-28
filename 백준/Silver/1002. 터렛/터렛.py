from sys import stdin
input = lambda: stdin.readline().rstrip()

for _ in range(int(input())):
 x1,y1,r1,x2,y2,r2=map(int, input().split())
 l=(x2-x1)**2+(y2-y1)**2
 if x1==x2 and y1==y2 and r1==r2:print(-1)
 elif l>(r1+r2)**2:print(0)
 elif l<(r2-r1)**2:print(0)
 elif l==(r2-r1)**2:print(1)
 elif l==(r1+r2)**2:print(1)
 else:print(2)