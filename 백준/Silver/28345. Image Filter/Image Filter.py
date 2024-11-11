def get_filtered_difference(H, r, c, R, C):
    A = H[r][c - 1] if c - 1 >= 0 else 0
    B = H[r - 1][c] if r - 1 >= 0 else 0
    C = H[r - 1][c - 1] if r - 1 >= 0 and c - 1 >= 0 else 0
    current_height = H[r][c]
    
    filters = [
        0,
        A,
        B,
        (A + B) // 2,
        A + B - C
    ]
    
    min_diff = float('inf')
    best_filter = 0
    best_value = 0
    for f_num, prediction in enumerate(filters):
        diff = current_height - prediction
        abs_diff = abs(diff)
        if abs_diff < min_diff or (abs_diff == min_diff and f_num < best_filter):
            min_diff = abs_diff
            best_filter = f_num
            best_value = diff
    
    return best_filter, best_value

from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    H = [ list(map(int, input().split())) for _ in range(R) ]
    
    for r in range(R):
        for c in range(C):
            best_filter, diff = get_filtered_difference(H, r, c, R, C)
            print(f"{best_filter} {diff}", end = " ")
        print()