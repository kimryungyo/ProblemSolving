from sys import stdin
input = lambda: stdin.readline()

def convert_24_to_seconds(time):
    h, m = map(int, time.split(":"))
    seconds = h * 3600 + m * 60
    return seconds

TC = int(input())
for tc in range(TC):
    T = int(input()) * 60
    NA, NB = map(int, input().split())

    events = []
    for _ in range(NA):
        start, end = map(convert_24_to_seconds, input().split())
        events.append( (start, True, 0) )
        events.append( (end + T, False, 1) )
    for _ in range(NB):
        start, end = map(convert_24_to_seconds, input().split())
        events.append( (start, True, 1) )
        events.append( (end + T, False, 0) )
    events.sort()

    starts = [0, 0]
    waits = [0, 0]

    for event in events:
        now, start, station = event
        if start:

            if not waits[station]:
                starts[station] += 1
                waits[station] += 1

            waits[station] -= 1

        else:
            waits[station] += 1

    print(f"Case #{tc + 1}: {starts[0]} {starts[1]}")