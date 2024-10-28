n = int(input())

k = n
cycle = None
for i in range(1, 10 ** 10):
    a, b = k // 10, k % 10
    c = a + b
    k = b * 10 + c % 10
    if k == n: break
print(i)