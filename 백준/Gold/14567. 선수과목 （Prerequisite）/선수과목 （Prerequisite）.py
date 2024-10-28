from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())

in_count = { num: 0 for num in range(1, N + 1) }
out_degree = { num: set() for num in range(1, N + 1) }

for _ in range(M):
    a, b = map(int, input().split())
    in_count[b] += 1
    out_degree[a].add(b)

queue = deque()
for num in range(1, N + 1):
    if in_count[num] == 0:
        queue.append(num)

order = []
semester = 0
semesters = deque([queue])
results = [None] * N

while semesters:
    semester += 1
    queue = semesters.popleft()
    next_queue = deque()

    while queue:
        vertex = queue.popleft()
        results[vertex - 1] = semester
        order.append(vertex)
        
        for next in out_degree[vertex]:
            in_count[next] -= 1
            if in_count[next] == 0:
                next_queue.append(next)

    if next_queue: semesters.append(next_queue)

print(" ".join(map(str, results)))