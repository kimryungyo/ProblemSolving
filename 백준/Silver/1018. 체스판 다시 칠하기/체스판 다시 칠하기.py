from sys import stdin
input = lambda: stdin.readline().rstrip()

def get_sub_board(y, x):
    sub_board = []
    for i in range(y, y + 8):
        line = []
        for j in range(x, x + 8):
            line.append(board[i][j])
        sub_board.append(line)
    return sub_board

def get_convert_count(board):
    min_count = float("inf")
    for target in ["W", "B"]:
        count = 0

        for i in range(8):
            for j in range(8):

                if board[i][j] != target:
                    count += 1
                
                if j != 8 -1:
                    target = "W" if target == "B" else "B"

        if count < min_count:
            min_count = count

    return min_count


n, m = map(int, input().split())
board = [ list(input()) for _ in range(n) ]

min_count = float("inf")
for y in range(n - 8 + 1):
    for x in range(m - 8 + 1):
        sub_board = get_sub_board(y, x)
        count = get_convert_count(sub_board)
        if count < min_count:
            min_count = count

print(min_count)
