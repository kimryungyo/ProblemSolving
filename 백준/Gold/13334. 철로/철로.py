from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
infos = {}
for num in range(n):
    start, end = sorted(map(int, input().split()))
    if start not in infos: infos[start] = []
    infos[start].append((num, start, "start"))
    
    if end not in infos: infos[end] = []
    infos[end].append((num, end, "end"))

events = sorted(infos.keys())
length = int(input())

started = set()
ended = set()

active = set()
max_count = 0

start = 0
for end in range(len(events)):

    min_pos = events[end] - length

    for bef in range(start, end):
        pos = events[bef]
        if pos >= min_pos: break

        for info in infos[pos]:
            num, _, type_ = info

            if num in active:
                active.remove(num)
                
            if num in started:
                started.remove(num)
                
            if num in ended:
                ended.remove(num)

        start += 1

    pos = events[end]
    for info in infos[pos]:
        num, _, type_ = info

        if type_ == "start":
            started.add(num)

        elif type_ == "end":
            ended.add(num)

            if num in started:
                active.add(num)

    count = len(active)
    if count > max_count:
        max_count = count

print(max_count)