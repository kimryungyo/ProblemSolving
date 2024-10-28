from sys import stdin
input = lambda: stdin.readline().rstrip()

def line_left_simulation(line):
    result = []
    stack = None
    for item in line:
        if item:
            if stack:
                if stack == item:
                    result.append(item * 2)
                    stack = None
                else:
                    result.append(stack)
                    stack = item
            else: stack = item
    
    if stack: result.append(stack)
    result += [0] * (8 - len(result))
    return result

class Board2048():
    def __init__(self, board):
        self.board = board

    def get_vertical(self, arr = None):
        if arr is None: arr = self.board
        lines = []
        for i in range(8):
            line = [ arr[j][i] for j in range(8) ]
            lines.append(line)
        return lines

    def get_horizontal(self, arr = None):
        if arr is None: arr = self.board
        return arr
    
    def move(self, dir):
        if dir == "L": 
            result = []
            lines = self.get_horizontal()
            for line in lines:
                sim_line = line_left_simulation(line)
                result.append(sim_line)
            self.board = result
    
        elif dir == "R":
            result = []
            lines = self.get_horizontal()
            for line in lines:
                line.reverse()
                sim_line = line_left_simulation(line)
                sim_line.reverse()

                result.append(sim_line)
            self.board = result

        elif dir == "U":
            ver_result = []
            lines = self.get_vertical()
            for line in lines:
                sim_line = line_left_simulation(line)
                ver_result.append(sim_line)
            result = self.get_vertical(ver_result)
            self.board = result

        elif dir == "D":
            ver_result = []
            lines = self.get_vertical()
            for line in lines:
                line.reverse()
                sim_line = line_left_simulation(line)
                sim_line.reverse()
                ver_result.append(sim_line)
            result = self.get_vertical(ver_result)
            self.board = result

    def print_board(self):
        print("\n".join(map(str, self.board)))

board_array = []
for _ in range(8):
    row = list(map(int, input().split()))
    board_array.append(row)

board = Board2048(board_array)
move = input()
board.move(move)
for line in board.board:
    for num in line:
        print(num, end = " ")
    print()