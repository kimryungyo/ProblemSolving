grid = [list(map(int, input().split())) for _ in range(9)]

max_value = -1
row, col = 0, 0

for i in range(9):
    for j in range(9):
        if grid[i][j] > max_value:
            max_value = grid[i][j]
            row = i + 1
            col = j + 1

print(max_value)
print(row, col)