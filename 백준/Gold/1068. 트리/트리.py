from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()

N, *parents, R = map(int, open(0).read().split())

childs = [ set() for _ in range(N) ]
for num, parent in enumerate(parents):
    if parent == -1: continue
    childs[parent].add(num)

if parents[R] == -1: print(0); quit()
childs[parents[R]].remove(R)

queue = deque([R])
while queue:
    node = queue.popleft()
    for child in childs[node]:
        queue.append(child)
    childs[node] = None

count = 0
for child in childs:
    if child == set():
        count += 1
print(count)