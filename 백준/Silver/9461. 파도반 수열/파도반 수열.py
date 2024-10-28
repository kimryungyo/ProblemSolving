from sys import stdin
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
 N=int(input());P=[0,1,1,1]
 for i in range(4, N+1): P.append(P[i-2] + P[i-3])
 print(P[N])