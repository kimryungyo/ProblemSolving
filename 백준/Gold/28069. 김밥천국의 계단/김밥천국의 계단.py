def move_stairs():
    total_stairs, moves = map(int, input().split())

    for i in range(moves - 1):
        remainder = total_stairs % 3

        if remainder == 2:
            total_stairs -= 1
        
        elif remainder == 1:
            total_stairs = int(total_stairs * 2/3) + 1

        else:
            total_stairs = total_stairs * 2/3

        if total_stairs == 1:
            break

    if total_stairs == 1:
        print("minigimbob")
    else:
        print("water")

move_stairs()
