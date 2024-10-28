from copy import deepcopy

n, m = map(int, input().split())

board = []
for _ in range(n):
    line = list(input())
    board.append(line)

def simulation(arr):
    passed = False
    last = None
    for i in range(len(arr)):
        pos = arr[i]

        if pos == "#": last = None

        elif pos == ".":
            if last is None:
                last = i

        elif pos == "O":
            last = True

        else:
            if last is True:
                if pos == "B":
                    return False
                
                elif pos == "R":
                    passed = True
            
            elif type(last) is int:
                arr[i] = "."
                arr[last] = pos
                last += 1
                
    if passed is True: return True
    return arr

def rotation_left(board):
    new_board = []
    for x in range(len(board[0]) - 1, -1, -1):
        line = []
        for y in range(len(board)):
            line.append( board[y][x] )
        new_board.append(line)
    return new_board


def rotation_right(board):
    new_board = []
    for x in range(len(board[0])):
        line = []
        for y in range(len(board) - 1, -1, -1):
            line.append( board[y][x] )
        new_board.append(line)
    return new_board




def sim_board_left(board):
    board = deepcopy(board)
    for i in range(len(board)):
        line = board[i]
        if ("R" in line) or ("B" in line):
            new_line = sim_left(line)
            if type(new_line) is not list: return new_line
            board[i] = new_line
    return board

def sim_board_right(board):
    board = deepcopy(board)
    for i in range(len(board)):
        line = board[i]
        if ("R" in line) or ("B" in line):
            new_line = sim_right(line)
            if type(new_line) is not list: return new_line
            board[i] = new_line
    return board



def sim_board_up(board):
    vert_lines = rotation_left(board)
    for i in range(len(vert_lines)):
        line = vert_lines[i]
        if ("R" in line) or ("B" in line):
            new_line = sim_left(line)
            if type(new_line) is not list: return new_line
            vert_lines[i] = new_line
    new_board = rotation_right(vert_lines)
    return new_board

def sim_board_down(board):
    vert_lines = rotation_left(board)
    for i in range(len(vert_lines)):
        line = vert_lines[i]
        if ("R" in line) or ("B" in line):
            new_line = sim_right(line)
            if type(new_line) is not list: return new_line
            vert_lines[i] = new_line
    new_board = rotation_right(vert_lines)
    return new_board

def sim_left(arr):
    return simulation(arr)

def sim_right(arr):
    arr = arr[::-1]
    arr = simulation(arr)
    if type(arr) is not list: return arr
    arr = arr[::-1]
    return arr

def print_board(board):
    for line in board:
        print("".join(line))

from collections import deque
queue = deque([ (["UP"], board), (["DOWN"], board), (["LEFT"], board), (["RIGHT"], board) ])

while queue:
    moves, board = queue.popleft()
    moves = moves.copy()
    move = moves[-1]

    if move == "UP":
        new_board = sim_board_up(board)
    elif move == "DOWN":
        new_board = sim_board_down(board)
    elif move == "LEFT":
        new_board = sim_board_left(board)
    elif move == "RIGHT":
        new_board = sim_board_right(board)

    if new_board is True:
        print(1); quit()
    
    if new_board is False:
        continue

    if board == new_board:
        continue

    if len(moves) < 10:
        for move in ["UP", "DOWN", "LEFT", "RIGHT"]:
            new_moves = moves + [move]

            next = (new_moves, new_board)
            queue.append(next)

print(0)