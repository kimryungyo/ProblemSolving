from sys import stdin
input = lambda: stdin.readline().rstrip()

N = int(input())
events = []

for _ in range(N):
    s, e = map(int, input().split())
    events.append(s * 2)
    events.append(e * 2 + 1)

events.sort()

length = active = start = end = 0
for event in events:
    pos, type = divmod(event, 2)

    if type == 0: 
        if not active: start = pos
        active += 1

    else:
        active -= 1
        if not active: length += pos - start

print(length)