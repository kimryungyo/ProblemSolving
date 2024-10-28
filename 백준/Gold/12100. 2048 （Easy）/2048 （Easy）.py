def line_left_simulation(line):
    global max_value
    result = []
    stack = None
    for item in line:
        if item:
            if stack:
                if stack == item:
                    if item * 2 > max_value:
                        max_value = item * 2
                    result.append(item * 2)
                    stack = None
                else:
                    result.append(stack)
                    stack = item
            else: stack = item
    
    if stack: result.append(stack)
    result += [0] * (n - len(result))
    return result

class Board2048():
    def __init__(self, board):
        self.board = board

    def get_vertical(self, arr = None):
        if arr is None: arr = self.board
        lines = []
        for i in range(n):
            line = [ arr[j][i] for j in range(n) ]
            lines.append(line)
        return lines

    def get_horizontal(self, arr = None):
        if arr is None: arr = self.board
        return arr
    
    def move(self, dir):
        if dir == 0: 
            result = []
            lines = self.get_horizontal()
            for line in lines:
                sim_line = line_left_simulation(line)
                result.append(sim_line)
            self.board = result
    
        elif dir == 1:
            result = []
            lines = self.get_horizontal()
            for line in lines:
                line.reverse()
                sim_line = line_left_simulation(line)
                sim_line.reverse()

                result.append(sim_line)
            self.board = result

        elif dir == 2:
            ver_result = []
            lines = self.get_vertical()
            for line in lines:
                sim_line = line_left_simulation(line)
                ver_result.append(sim_line)
            result = self.get_vertical(ver_result)
            self.board = result

        elif dir == 3:
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

n = int(input())
max_value = 0

board_array = []
for _ in range(n):
    row = list(map(int, input().split()))
    if max(row) > max_value: max_value = max(row)
    board_array.append(row)

for i in range(4):
    step1 = Board2048(board_array)
    step1.move(i)

    for j in range(4):
        step2 = Board2048(step1.board)
        step2.move(j)

        for k in range(4):
            step3 = Board2048(step2.board)
            step3.move(k)

            for l in range(4):
                step4 = Board2048(step3.board)
                step4.move(l)

                for m in range(4):
                    step5 = Board2048(step4.board)
                    step5.move(m)

print(max_value)