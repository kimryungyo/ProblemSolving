import sys; input = lambda: sys.stdin.readline().rstrip()
while(n:=int(input()))>0:print(min((input()for _ in'_'*n),key=str.lower))