from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()

N = int(input())

vertices = { num for num in range(N) }
in_degree = { num: set() for num in range(N) }
out_degree = { num: set() for num in range(N) }

for _ in range(N - 1):
    a, b = map(int, input().split())
    in_degree[a].add(b)
    in_degree[b].add(a)
    out_degree[a].add(b)
    out_degree[b].add(a)

def is_edge_vertex(num):
    if len(in_degree[num]) == len(out_degree[num]) == 1:
        if in_degree[num] == out_degree[num]:
            return True
    return False

edge_vertex = set()
for num in range(N):
    if is_edge_vertex(num):
        edge_vertex.add(num)

queue = deque([ edge_vertex ])
while queue:
    edge_vertex = queue.popleft()

    if len(edge_vertex) <= 2:
        print(" ".join(map(str, sorted(vertices))))
        quit()

    vertices -= edge_vertex

    next_vertex = set()
    for remove in edge_vertex:
        out = out_degree[remove].pop()
        in_degree[out].remove(remove)
        out_degree[out].remove(remove)

        if is_edge_vertex(out):
            next_vertex.add(out)


    queue.append(next_vertex)