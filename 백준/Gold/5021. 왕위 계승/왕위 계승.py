from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
adam = input()

lineage = { adam: 1 }
graph = {}
childs = {}
people = { adam }

for _ in range(N):
    child, parent_1, parent_2 = input().split()
    childs[child] = [parent_1, parent_2]

    if parent_1 not in graph: graph[parent_1] = []
    graph[parent_1].append(child)

    if parent_2 not in graph: graph[parent_2] = []
    graph[parent_2].append(child)

    people.add(child)
    people.add(parent_1)
    people.add(parent_2)

parents = deque([ adam ])
while parents:
    parent = parents.popleft()
    if parent in graph:
        for child in graph[parent]:
            blood = (lineage.get(childs[child][0], 0) + lineage.get(childs[child][1], 0)) / 2
            lineage[child] = blood
            parents.append(child)

candidates = [ input() for _ in range(M) ]
elected = max(candidates, key=lambda name: lineage.get(name, 0))
print(elected)