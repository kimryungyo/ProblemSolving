from heapq import heappop, heappush
from sys import stdin
input = lambda: stdin.readline().rstrip()

N = int(input())
cows = [ tuple(map(int, input().split())) for _ in range(N) ]

cows = [(i, interval[0], interval[1]) for i, interval in enumerate(cows)]
cows.sort(key=lambda x: x[1])

able_rooms = []
used_rooms = [0] * N
room_count = 0

for i, start, end in cows:
    if able_rooms and able_rooms[0][0] < start:
        ear_end, room_num = heappop(able_rooms)
        used_rooms[i] = room_num
        heappush(able_rooms, (end, room_num))
    else:
        room_count += 1
        used_rooms[i] = room_count
        heappush(able_rooms, (end, room_count))

print(room_count)
for num in used_rooms:
    print(num)