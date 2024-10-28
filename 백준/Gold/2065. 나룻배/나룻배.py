from collections import deque

from sys import stdin
input = lambda: stdin.readline().rstrip()

m, t, n = map(int, input().split())
guests = deque()
for num in range(n):
    a, b = input().split()
    arrival = int(a)
    position = b
    guests.append((num, arrival, position))

time = 0
boat_pos = "left"
other_pos = {"left": "right", "right": "left"}
waiting = {"left": deque(), "right": deque()}
on_boat = []
arrivals = []


def send_time(send):
    global time
    time += send
    if guests:
        while guests[0][1] <= time:
            guest = guests.popleft()
            waiting[guest[2]].append(guest)
            if not guests: break

def pick_up():
    global boat_pos
    for _ in range( min(len(waiting[boat_pos]), m) ):
        guest = waiting[boat_pos].popleft()
        on_boat.append(guest)

def move():
    global boat_pos, on_boat
    if boat_pos == "left": boat_pos = "right"
    elif boat_pos == "right": boat_pos = "left"
    send_time(t)
    
    if on_boat:
        for guest in on_boat:
            arrivals.append(guest + (time,))
        on_boat = []

def is_waiting(pos):
    return bool(waiting[pos])

while is_waiting("left") or is_waiting("right") or guests:

    if not (is_waiting("left") or is_waiting("right")):
        next_time = guests[0][1]
        send_time(next_time - time)
        continue

    if is_waiting(boat_pos) is False:
        move()
        pick_up()
        move()
        continue

    else:
        pick_up()
        move()
        continue

def print_result():
    arrivals.sort(key=lambda x: x[0])
    print(*map(lambda x: x[3], arrivals), sep = "\n")
    quit()

print_result()