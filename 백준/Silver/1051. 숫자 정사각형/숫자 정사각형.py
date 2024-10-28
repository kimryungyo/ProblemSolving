n, m = map(int, input().split())
array = []
for _ in range(n): array.append(list(input()))

max_size = -1
for y in range(n):
    for x in range(m):
        for size in range( max_size + 1, min(n - y, m - x) ):
            if array[y][x] == array[y + size][x] == array[y][x + size] == array[y + size][x + size]:
                max_size = size
max_size += 1

print(max_size ** 2)