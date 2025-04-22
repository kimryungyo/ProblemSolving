K, N, M = map(int, input().split())
total_cost = K * N
print(max(0, total_cost - M))