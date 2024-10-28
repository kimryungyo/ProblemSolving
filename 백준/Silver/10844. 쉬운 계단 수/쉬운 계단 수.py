dp = { (0, 0): 1, (1, 0): 1, (2, 0): 1, (3, 0): 1, (4, 0): 1, (5, 0): 1, (6, 0): 1, (7, 0): 1, (8, 0): 1, (9, 0): 1}

for i in range(1, 100):
    for j in range(0, 10):
        count = 0
        if j > 0: count += dp[(j-1, i-1)]
        if j < 9: count += dp[(j+1, i-1)]
        dp[(j, i)] = count

total = 0
length = int(input())
for i in range(1, 10):
    total += dp[(i, length - 1)]

print(total % 1000000000)