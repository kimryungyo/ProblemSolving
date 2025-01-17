from collections import defaultdict

N, M, T = map(int, input().split())
clipboard = [input() for _ in range(N)]

groups = defaultdict(list)

for x in range(N):
    for y in range(M):
        color = clipboard[x][y]
        if color == '.':
            continue
        d = x - y
        groups[d].append((x, color))

color_count = {'R': 0, 'G': 0, 'B': 0}

for d, arr in groups.items():
    arr.sort(key=lambda e: e[0])
    
    prev_x = None
    for idx, (x_j, c_j) in enumerate(arr):
        if idx == 0:
            count_here = T
        else:
            x_prev = arr[idx-1][0]
            delta = x_j - x_prev
            count_here = min(delta, T)
        
        color_count[c_j] += count_here

print(color_count['R'])
print(color_count['G'])
print(color_count['B'])