from itertools import combinations
N = int(input())

results = []
for a in range(1, 10 + 1):
	for b in combinations(range(10), a):
		num = ''.join(list(map(str, reversed(list(b)))))
		results.append(int(num))

results.sort()
if N >= len(results): print(-1)
else: print(results[N])