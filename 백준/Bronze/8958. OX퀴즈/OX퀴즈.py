for _ in range(int(input())):
    result = input()
    score = 0
    combo = 0
    for r in result:
        if r == 'O':
            combo += 1
            score += combo
        else:
            combo = 0
    print(score)