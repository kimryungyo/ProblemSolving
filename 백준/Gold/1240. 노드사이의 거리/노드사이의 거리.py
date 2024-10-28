import math
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())

LOG = int(math.log2(N)) + 1
D = [ 0 ] * (N + 1)
V = [ False ] * (N + 1)
P = [ [0] * LOG for _ in range(N + 1) ]
L = [ 0 ] * (N + 1)

G = [ [] for _ in range(N + 1) ]
for _ in range(N - 1):
  a, b, c = map(int, input().split())
  G[a].append((b, c))
  G[b].append((a, c))

def dfs(n = 1, d = 0, l = 0):
  V[n] = True
  D[n] = d
  L[n] = l

  for next, leng in G[n]:
    if V[next]: continue
    P[next][0] = n
    dfs(next, d + 1, l + leng)

def set_parents():
  dfs()
  for i in range(1, LOG):
    for j in range(1, N + 1):
      P[j][i] = P[P[j][i - 1]][i - 1]

def lca(a, b):
  if D[a] > D[b]: a, b = b, a
  for i in range(LOG - 1, -1, -1):
    if D[b] - D[a] >= (2 ** i):
      b = P[b][i]

  if a == b: return a
  
  for i in range(LOG - 1, -1, -1):
    if P[a][i] != P[b][i]:
      a = P[a][i]
      b = P[b][i]
  return P[a][0]

set_parents()

for _ in range(M):
  a, b = map(int, input().split())
  lca_ = lca(a, b)
  a_d = abs(L[lca_] - L[a])
  b_d = abs(L[lca_] - L[b])
  print(a_d + b_d)