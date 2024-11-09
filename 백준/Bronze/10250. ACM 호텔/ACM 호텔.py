T = int(input())
for _ in range(T):
    h, w, n = map(int, input().strip().split())
    
    floor = n % h
    if floor == 0:
        floor = h

    room = (n // h) + 1
    if n % h == 0:
        room -= 1
    
    room_number = floor * 100 + room
    print(room_number)