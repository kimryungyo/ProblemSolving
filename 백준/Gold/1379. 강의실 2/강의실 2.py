from sys import stdin
input = lambda: stdin.readline().rstrip()

N = int(input())
classes = []
used_rooms = [ 0 ] * (N + 1)
rooms = [ 2 ]
able_rooms = set()

for _ in range(N):
    n, s, e = map(int, input().split())
    classes.append( (s, True, n) )
    classes.append( (e, False, n) )

classes.sort()

active = 0
max_active = 0
for pos, type, num in classes:
    if type is True:
        if not able_rooms:
            rooms.append(0)
            able_rooms.add(len(rooms) - 1)
        use_room = able_rooms.pop()

        rooms[use_room] -= 1
        if rooms[use_room] > 0: 
            able_rooms.add(use_room)
        used_rooms[num] = use_room

    else:
        used_room = used_rooms[num]
        rooms[used_room] -= 1
        able_rooms.add(used_room)

print(len(rooms) - 1)
for i in range(1, len(used_rooms)):
    print(used_rooms[i])