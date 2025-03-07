N = int(input())
total = 0

for _ in range(N):
    score_str = input()
    
    modified = ''.join('9' if ch in '069' else ch for ch in score_str)
    score = int(modified)
    
    if score > 100:
        score = 100
    total += score

avg = total / N

result = int(avg + 0.5)
print(result)