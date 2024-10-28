N, M = map(int, input().split())
opinions = [input() for _ in range(N)]
count = 0

for opinion in opinions:
    agree_count = 0
    for o in opinion:
        if o == 'O':
            agree_count += 1

    if agree_count > M // 2:
        count += 1

print(count)