def find_sum(N):
    total_sum = 0
    for q in range(1, N):
        x = q * (N + 1)
        total_sum += x
    return total_sum

N = int(input().strip())
print(find_sum(N))