from collections import deque

n, m = map(int, input().split())
pool = {}
heights = []

for h in range(2, 10):
    pool[h] = { "walls": set(), "voids": set() }

for y in range(n):
    floor = input()
    for x in range(len(floor)):
        block = int(floor[x])
        position = (x, y)

        for h in range(2, 10):
            if block >= h:
                pool[h]["walls"].add(position)

            else:
                pool[h]["voids"].add(position)

moves = ( (0, 1), (0, -1), (1, 0), (-1, 0) )
way_count = {}

count = 0

for h in range(2, 10):

    walls = pool[h]["walls"]
    voids = pool[h]["voids"]

    while voids:
        is_border = False
        root = voids.pop()
        
        group = []
        group_count = 0
        
        queue = deque([root])
        while queue:
            block = queue.popleft()
            group.append(block)
            group_count += 1

            for move in moves:
                next = (block[0] + move[0], block[1] + move[1])

                if is_border is False:
                    if (next[0] < 0) or (next[0] > m - 1):
                        is_border = True

                    if (next[1] < 0) or (next[1] > n - 1):
                        is_border = True

                if next in voids:
                    voids.remove(next)
                    queue.append(next)

        if is_border is False:
            count += group_count

print(count)