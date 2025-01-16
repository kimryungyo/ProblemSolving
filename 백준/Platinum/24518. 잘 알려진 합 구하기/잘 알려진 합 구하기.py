MAX = 10 ** 9
MOD = 10 ** 9 + 7
N, M = map(int, input().split())

def binary_search(func, value, min_val, max_val, lower=True, reverse=False):
    result = -1
    while min_val <= max_val:
        mid = (min_val + max_val) // 2
        f_mid = func(mid)

        if f_mid == value:
            result = mid
            if lower: max_val = mid - 1
            else: min_val = mid + 1
        else:
            if reverse:
                if f_mid < value: max_val = mid - 1
                else: min_val = mid + 1
            else:
                if f_mid < value: min_val = mid + 1
                else: max_val = mid - 1

    return result

def sum_g(M, i, j):
    cycle_sum = M * (M - 1) // 2
    
    cycle_i = i // M
    cycle_j = j // M
    
    pos_i = i % M
    pos_j = j % M
    
    total = 0
    
    if cycle_i == cycle_j:
        n = pos_j - pos_i + 1
        total = n * (pos_i + pos_j) // 2
    else:
        n1 = M - pos_i
        total += n1 * (pos_i + (M - 1)) // 2
        
        full_cycles = cycle_j - cycle_i - 1
        if full_cycles > 0:
            total += full_cycles * cycle_sum
        
        n2 = pos_j + 1
        total += n2 * (0 + pos_j) // 2
    
    return total

f = lambda i: N // i
g = lambda i: i % M

f_idx = lambda i, lower: binary_search(f, i, 1, MAX, lower, reverse=True)

answer = 0
f_value = N
while True:
    left, right = f_idx(f_value, True), f_idx(f_value, False)

    count = right - left + 1
    g_sum = sum_g(M, left, right)

    add = f_value * g_sum
    answer += add
    answer %= MOD

    if right == N: break
    f_value = f(right + 1)

print(answer)