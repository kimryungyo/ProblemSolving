n = int(input())
snowballs = list(map(int, input().split()))

cases = []
for i in range(len(snowballs)):
    for j in range(i + 1, len(snowballs)):
        cases.append( ( (i, j), (snowballs[i], snowballs[j]), snowballs[i] + snowballs[j] ) )

cases.sort(key=lambda x: x[2])

min_diff = float('inf')
for i in range(len(cases) - 1):
    for j in range(i + 1, len(cases)):
        if len(set(cases[i][0]) & set(cases[j][0])) == 0:
            diff = cases[j][2] - cases[i][2]
            if diff < min_diff: min_diff = diff
            break

print(min_diff)