from sys import stdin
input = stdin.readline

N = int(input())
if N == 2: print(1, 1); quit()

grid = [ list(map(int, input().split())) for _ in range(N) ]
array = [0] * N

for i in range(N):

    a, b = 0, 1
    if i == 0: a, b = 1, 2
    elif i == 1: a, b = 0, 2

    a_i_sum = grid[i][a]
    b_i_sum = grid[i][b]
    a_b_sum = grid[a][b]

    num = (a_i_sum + b_i_sum - a_b_sum) // 2
    array[i] = num

print(" ".join(map(str, array)))