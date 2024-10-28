from sys import stdin
input = stdin.readline

N = int(input())
M = []
for num in range(1, N + 1):
  w, h = map(int, input().split())
  ppi = (w**2+h**2)**0.5/24
  M.append((-ppi, num))
M.sort()

for ppi, num in M: print(num)