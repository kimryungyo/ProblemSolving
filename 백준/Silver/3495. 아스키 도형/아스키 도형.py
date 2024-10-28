from sys import stdin
input = lambda: stdin.readline().rstrip()

n, m = map(int, input().split())

board = [input() for _ in range(n)]

ans = 0
for i in range(n):
    sum = 0
    for j in range(m):
        if board[i][j] == '/' or board[i][j] == '\\':
            sum += 1
            ans += 1
        if sum % 2 == 1 and board[i][j] == '.':
            ans += 2

print(ans // 2)