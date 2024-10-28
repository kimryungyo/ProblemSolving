from itertools import combinations

n = int(input())
factorials = [1, 1]

i = 1
while factorials[-1] <= n:
    i += 1
    factorials.append(factorials[-1] * i)

for m in range(1, len(factorials)+1):
    for comb in combinations(factorials, m):
        if sum(comb) == n:
            print("YES")
            quit()

print("NO")
