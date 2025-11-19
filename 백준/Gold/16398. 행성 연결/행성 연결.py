from sys import stdin
input = stdin.readline

N = int(input())
graph = [ list(map(int, input().split())) for _ in range(N) ]
edges = []

for i in range(N):
    for j in range(i, N):
        edges.append( (graph[i][j], i, j) )


def union_finder(node):
    if node == union[node]:
        return node
    union[node] = union_finder(union[node])
    return union[node]

union = [ i for i in range(N) ]
edges.sort()

total = 0
for price, a, b in edges:
    au, bu = union_finder(a), union_finder(b)
    if au == bu: continue

    union[au] = bu
    total += price

print(total)