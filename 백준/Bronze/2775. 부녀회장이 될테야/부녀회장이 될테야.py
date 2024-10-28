T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    floors = [ [ i for i in range(1, n + 1) ] ]

    for floor in range(1, k + 1):
        before_floor = floors[floor - 1]
        new_floor = []

        sum_ = 0
        for number in range(1, n + 1):
            sum_ += before_floor[number - 1]
            new_floor.append(sum_)

        floors.append(new_floor)

    print(sum_)