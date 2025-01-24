from collections import deque

N = int(input())
space = [ list(map(int, input().split())) for _ in range(N) ]

directions = [0, 0, 1, -1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

shark_x, shark_y, shark_size = 0, 0, 2

for row in range(N):
    for col in range(N):
        if space[row][col] == 9:
            shark_x, shark_y = row, col
            break
    else:
        continue
    break

space[shark_x][shark_y] = 0
fish_eaten = 0
total_time = 0

def find_fish(x, y, size):
    distance = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    edible_fishes = []

    while queue:
        current_x, current_y = queue.popleft()
        for i in range(4):
            new_x = current_x + dx[i]
            new_y = current_y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N and not visited[new_x][new_y]:
                if space[new_x][new_y] <= size:
                    queue.append((new_x, new_y))
                    visited[new_x][new_y] = True
                    distance[new_x][new_y] = distance[current_x][current_y] + 1
                    if 0 < space[new_x][new_y] < size:
                        edible_fishes.append((new_x, new_y, distance[new_x][new_y]))
                        
    edible_fishes.sort(key=lambda fish: (fish[2], fish[0], fish[1]))
    return edible_fishes

while True:
    fishes = find_fish(shark_x, shark_y, shark_size)
    if not fishes:
        break
    target_fish = fishes[0]
    fish_x, fish_y, distance = target_fish
    total_time += distance
    fish_eaten += 1
    space[fish_x][fish_y] = 0
    shark_x, shark_y = fish_x, fish_y
    if fish_eaten == shark_size:
        shark_size += 1
        fish_eaten = 0

print(total_time)