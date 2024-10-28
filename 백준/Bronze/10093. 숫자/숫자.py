a, b = map(int, input().split())
min = min(a, b)
max = max(a, b)
n = max-min-1
if min == max or min+1 == max: n = 0    
print(n)
for i in range(min+1, max):
    print(i, end = ' ')