t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    s = a + b
    m = (s - 1) * s // 2
    print(m * s)