board_size = 0
board = []

used_block = [False] * 5
blocks = [[] for _ in range(5)]

visited = set()

min_answer = ""

def in_range(row, col):
    if row < 0 or row >= board_size:
        return False
    if col < 0 or col >= board_size:
        return False
    return True

def check(start_row, start_col, block_num):
    for i in range(len(blocks[block_num])):
        for j in range(len(blocks[block_num][i])):
            if not in_range(start_row + i, start_col + j):
                return False
            if blocks[block_num][i][j] == '#' and board[start_row + i][start_col + j] != '0':
                return False
    return True

def fill(start_row, start_col, block_num):
    for i in range(len(blocks[block_num])):
        for j in range(len(blocks[block_num][i])):
            if blocks[block_num][i][j] == '#':
                board[start_row + i] = board[start_row + i][:start_col + j] + str(block_num + 1) + board[start_row + i][start_col + j + 1:]

def empty(start_row, start_col, block_num):
    for i in range(len(blocks[block_num])):
        for j in range(len(blocks[block_num][i])):
            if blocks[block_num][i][j] == '#':
                board[start_row + i] = board[start_row + i][:start_col + j] + '0' + board[start_row + i][start_col + j + 1:]

def is_solved():
    for i in range(5):
        if not used_block[i]:
            return False
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == '0':
                return False
    return True

def solve():
    global min_answer
    current_board = "".join(board)
    if is_solved():
        min_answer = min(min_answer, current_board)
        return
    if current_board in visited:
        return
    visited.add(current_board)
    if current_board > min_answer:
        return
    for r in range(board_size):
        for c in range(board_size):
            if board[r][c] == '0':
                for block_num in range(5):
                    if used_block[block_num]:
                        continue
                    start_col = 0
                    for i in range(len(blocks[block_num][0])):
                        if blocks[block_num][0][i] == '#':
                            start_col = c - i
                            break
                    if not check(r, start_col, block_num):
                        continue
                    used_block[block_num] = True
                    fill(r, start_col, block_num)
                    next_board = "".join(board)
                    if next_board not in visited and next_board < min_answer:
                        solve()
                    used_block[block_num] = False
                    empty(r, start_col, block_num)
                break

board_size = int(input())
for _ in range(board_size):
    board.append("0" * board_size)
min_answer = "6" * (board_size * board_size)
no_answer = "6" * (board_size * board_size)
for i in range(5):
    n, m = map(int, input().split())
    for _ in range(n):
        blocks[i].append(input())
solve()
if min_answer == no_answer:
    print("gg")
else:
    for i in range(0, board_size * board_size, board_size):
        print(min_answer[i:i+board_size])