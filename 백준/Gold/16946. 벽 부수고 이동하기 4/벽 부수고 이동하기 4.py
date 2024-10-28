from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()

n, m = map(int, input().split())
ways = set()
walls = set()
for y in range(n):
    codes = list(input())
    for x in range(m):
        if codes[x] == "0":
            ways.add( (x, y) )
        else:
            walls.add( (x, y) )

moves = ( (0, 1), (0, -1), (1, 0), (-1, 0) )
way_count = {}

while ways:
    root = ways.pop()
    
    group = []
    group_count = 0
    
    queue = deque([root])
    while queue:
        block = queue.popleft()
        group.append(block)
        group_count += 1

        for move in moves:
            next = (block[0] + move[0], block[1] + move[1])
            if next in ways:
                ways.remove(next)
                queue.append(next)

    for block in group:
        way_count[block] = (group_count, root)

values = {}
for wall in walls:
    value = 1
    roots = set()

    for move in moves:
        around = (wall[0] + move[0], wall[1] + move[1])

        if around in way_count:
            if way_count[around][1] not in roots:
                value += way_count[around][0]
                roots.add(way_count[around][1])

    values[wall] = value

for y in range(n):
    for x in range(m):
        block = (x, y)
        if block in values:
            print(values[block] % 10, end = "")
        else:
            print(0, end = "")
    print("")