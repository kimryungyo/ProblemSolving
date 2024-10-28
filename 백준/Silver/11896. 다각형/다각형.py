A, B = map(int, input().split())
if B < 4: result = 0
else:
    if A < 4: A = 4
    if A % 2 == 1: A += 1
    if B % 2 == 1: B -= 1
    result = ((B // 2) - (A // 2) + 1) * ((A // 2) + (B // 2))
print(result)