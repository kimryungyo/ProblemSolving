dice = list(map(int, input().split()))

if dice[0] == dice[1] == dice[2]:
    prize = 10000 + dice[0] * 1000
elif dice[0] == dice[1] or dice[0] == dice[2] or dice[1] == dice[2]:
    if dice[0] == dice[1]:
        prize = 1000 + dice[0] * 100
    elif dice[0] == dice[2]:
        prize = 1000 + dice[0] * 100
    else:
        prize = 1000 + dice[1] * 100
else:
    prize = max(dice) * 100

print(prize)
