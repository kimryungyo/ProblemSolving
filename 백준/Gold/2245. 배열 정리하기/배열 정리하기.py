from collections import deque

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

counts = [0] * (n + 1)
for i in range(n):
    counts[A[i]] += 1
    counts[B[i]] += 1

for i in range(1, n + 1):
    if counts[i] != 2:
        print(-1)
        quit()

positions = [[] for _ in range(n + 1)]
for i in range(n):
    positions[A[i]].append((i, 0))
    positions[B[i]].append((i, 1))

graph = [[] for _ in range(n)]
for value in range(1, n + 1):
    (i, arr_i), (j, arr_j) = positions[value][0], positions[value][1]
    
    if i == j:
        continue
    
    weight = 1 if arr_i == arr_j else 0
    graph[i].append((j, weight))
    graph[j].append((i, weight))

swaped = [-1] * n
answer = 0

for i in range(n):
    if swaped[i] != -1: continue

    if not graph[i]:
        swaped[i] = 0
        continue

    queue = deque([i])
    swaped[i] = 0
    groups = []

    while queue:
        current = queue.popleft()
        groups.append(current)

        for next, weight in graph[current]:
            action = swaped[current] if weight == 0 else 1 - swaped[current]

            if swaped[next] == -1:
                swaped[next] = action
                queue.append(next)

            elif swaped[next] != action:
                print(-1)
                quit()

    swaps_count = sum(swaped[node] for node in groups)
    non_swaps_count = len(groups) - swaps_count
    answer += min(swaps_count, non_swaps_count)

print(answer)