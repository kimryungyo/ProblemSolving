def third_largest_value(test_cases):
    results = []
    for case in test_cases:
        sorted_case = sorted(case, reverse=True)
        results.append(sorted_case[2])
    return results

import sys
input = sys.stdin.read

data = input().split()
T = int(data[0])

index = 1
test_cases = []

for _ in range(T):
    test_cases.append(list(map(int, data[index:index + 10])))
    index += 10

results = third_largest_value(test_cases)

for result in results:
    print(result)