for _ in range(int(input())):
    a, b, c = map(int, input().split())
    count = 0
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            for z in range(1, c + 1):
                if x % y != 0: continue
                if y % z != 0: continue
                if z % x != 0: continue
                count += 1
    print(count)