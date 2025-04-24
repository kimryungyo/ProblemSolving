a, b = input().split()
la, lb = len(a), len(b)
ans = la
for i in range(lb - la + 1):
    diff = 0
    for x, y in zip(a, b[i:i + la]):
        if x != y: diff += 1
            
    if diff < ans: ans = diff
print(ans)