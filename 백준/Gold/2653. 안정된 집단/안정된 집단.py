# 출처 : https://way-code.tistory.com/entry/%EB%B0%B1%EC%A4%80-2653%EB%B2%88-%EC%95%88%EC%A0%95%EB%90%9C-%EC%A7%91%EB%8B%A8-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys; readline = sys.stdin.readline

n = int(readline())
relation = [list(map(int, readline().split())) for _ in range(n)]

stable = True
for i in range(n):
    for j in range(i + 1, n):
        if relation[i][j] != relation[j][i]:
            stable = False
            break
    if not stable: break

visited = [False] * n
group = []
count = 0
for i in range(n):
    if visited[i]:
        continue

    visited[i] = True
    count += 1
    group.append([i+1])
    g_index = count - 1
    for j in range(n):
        if relation[i][j] != 0 or i == j:
            continue

        group[g_index].append(j+1)
        visited[j] = True

for g in group:
    if len(g) < 2:
        stable = False
        break

if stable:
    print(count)
    for g in group:
        print(*g)
else:
    print(0)