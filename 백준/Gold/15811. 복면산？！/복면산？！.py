from itertools import permutations

expressions = [0] * 100
results = [0] * 100

A, B, C = map(list, input().split())
chars = list(set(A + B + C))
asciis = list(map(ord, chars))
nums = [ num for num in range(10) ]

for power in range(len(A)): expressions[ord(A.pop())] += 10 ** power
for power in range(len(B)): expressions[ord(B.pop())] += 10 ** power
for power in range(len(C)): results[ord(C.pop())] += 10 ** power

count = 0
for matchs in permutations(nums, len(chars)):
    expression = result = 0

    for i in range(len(chars)):
        ascii = asciis[i]
        weight = matchs[i]
        expression += expressions[ascii] * weight
        result += results[ascii] * weight

    if expression == result:
        count += 1
        print("YES")
        quit()

print("NO")