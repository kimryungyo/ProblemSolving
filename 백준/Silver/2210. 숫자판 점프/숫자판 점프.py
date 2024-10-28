directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
paths = []
for dir1 in directions :
    for dir2 in directions:
        for dir3 in directions:
            for dir4 in directions:
                for dir5 in directions:
                    paths.append((dir1, dir2, dir3, dir4, dir5))

grid = []
for i in range(5): grid.append(input().split())

def get_numbers(x, y, path):
    number = grid[x][y]
    for step in path:
        if 0 <= (x := x + step[0]) <= 4 and 0 <= (y := y + step[1]) <= 4:
            number += grid[x][y]
        else: return None
    return number

numbers = set()
for x in range(5):
    for y in range(5):
        for path in paths:
            if (result := get_numbers(x, y, path)) != None:
                numbers.add(result)

print(len(numbers))
