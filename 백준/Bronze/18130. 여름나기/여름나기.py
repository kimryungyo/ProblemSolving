from sys import stdin
input = stdin.readline

def total_cost(P, K, C, Q):
    price = P
    pay_count = Q // K
    if Q % K == 0: pay_count -= 1

    price += ((pay_count * (pay_count + 1)) // 2) * C
    return price

N, Q = map(int, input().split())
fans = []
for _ in range(N):
    P, K, C = map(int, input().split())
    fans.append((P, K, C))

min_cost = float('inf')
min_index = -1

for i, (P, K, C) in enumerate(fans, 1):
    cost = total_cost(P, K, C, Q)
    if cost < min_cost:
        min_cost = cost
        min_index = i

print(min_index, min_cost)