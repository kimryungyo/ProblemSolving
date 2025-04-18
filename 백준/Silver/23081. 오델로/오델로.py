from sys import stdin
input = lambda: stdin.readline().rstrip()

N = int(input())
board = [list(input()) for _ in range(N)]

dirs = [ (1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1) ]
max_flips = ans_x = ans_y = 0

for y in range(N):
    for x in range(N):
        if board[y][x] != '.': continue
            
        total = 0
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            cnt = 0
            
            while 0 <= nx < N and 0 <= ny < N and board[ny][nx] == 'W':
                cnt += 1
                nx += dx
                ny += dy
                
            if cnt > 0 and 0 <= nx < N and 0 <= ny < N and board[ny][nx] == 'B':
                total += cnt
                
        if total > max_flips:
            max_flips = total
            ans_x = x
            ans_y = y
            
if max_flips > 0:
    print(ans_x, ans_y)
    print(max_flips)
else:
    print("PASS")
