from sys import stdin
input = lambda: stdin.readline().rstrip()

def is_across_start(grid, i, j):
    if j == 0 or grid[i][j-1] == '#':
        if j+2 < len(grid[0]) and grid[i][j] == '.' and grid[i][j+1] == '.' and grid[i][j+2] == '.':
            return True
    return False

def is_down_start(grid, i, j):
    if i == 0 or grid[i-1][j] == '#':
        if i+2 < len(grid) and grid[i][j] == '.' and grid[i+1][j] == '.' and grid[i+2][j] == '.':
            return True
    return False

def solve_crossword(grid):
    clues = []
    clue_number = 1

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.' and (is_across_start(grid, i, j) or is_down_start(grid, i, j)):
                clues.append((i+1, j+1))
                clue_number += 1

    return clues

N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

clues = solve_crossword(grid)

print(len(clues))
for clue in clues:
    print(f"{clue[0]} {clue[1]}")