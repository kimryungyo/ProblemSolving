table = [ [0] * 1001 for _ in range(1001) ]
n = int(input())

for i in range(1, n+1):
    a, b, w, h = map(int, input().split())
    for y in range(b, b + h):
        table[y][a:a + w] = [i] * w
            
for i in range(1, n + 1):
    count = 0
    for l in range(1001): count += table[l].count(i)
    print(count)