from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
events = []

heights = set( [ 0 ] )
actives = { 0: 1 }

for _ in range(n):
    left, height, right = map(int, input().split())
    heights.add(height)
    actives[height] = 0
    events.append( (left, False, height) )
    events.append( (right, True, height) )

events.sort()
heights = sorted(heights)
height_idxs = { height: idx for idx, height in enumerate(heights) }
max = 0


first_height = 0
first_pos = 0
start_idx = 0
for i in range(len(events)):
    event = events[i]
    pos, type, height = event
    if pos != events[0][0]: break
    actives[height] += 1
    if height > first_height:
        first_height = height
        first_pos = pos
    start_idx = i

print(first_pos, first_height, end = " ")

bef = height_idxs[first_height]
top = height_idxs[first_height]

for i in range(start_idx + 1, len(events)):
    event = events[i]
    pos, type, height = event
    if type is False:
        actives[height] += 1

        if height > heights[top]:
            top = height_idxs[height] 

    else: 
        actives[height] -= 1
        while actives[heights[top]] == 0: top -= 1

    if bef != top: 
        print(pos, heights[top], end = " ")

    bef = top