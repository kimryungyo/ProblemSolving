table = [ [ "." for _ in range(9) ] for _ in range(9) ]
possible = [ [ { i for i in range(1, 10) } for _ in range(9) ] for _ in range(9) ]

def valid_sudoku():
    for a in range(3):
        for b in range(3):

            possibles = set()
            need_numbers = { i for i in range(1, 10) }

            for i in range(3):
                for j in range(3):
                    x = a * 3 + i
                    y = b * 3 + j
                    
                    num = table[y][x]
                    possibles |= possible[y][x]
                    if num in need_numbers:
                        need_numbers.remove(num)

            for num in need_numbers:
                if num not in possibles:
                    print("ERROR")
                    quit()

    for x in range(9):
        possibles = set()
        need_numbers = { i for i in range(1, 10) }

        for y in range(9):
            num = table[y][x]
            possibles |= possible[y][x]
            if num in need_numbers:
                need_numbers.remove(num)

        for num in need_numbers:
            if num not in possibles:
                print("ERROR")
                quit()

    for y in range(9):
        possibles = set()
        need_numbers = { i for i in range(1, 10) }

        for x in range(9):
            num = table[y][x]
            possibles |= possible[y][x]
            if num in need_numbers:
                need_numbers.remove(num)

        for num in need_numbers:
            if num not in possibles:
                print("ERROR")
                quit()


def add(x, y, v):
    table[y][x] = v
    possible[y][x] = set()

    for i in range(9):
        if v in possible[y][i]:
            possible[y][i].remove(v)

    for i in range(9):
        if v in possible[i][x]:
            possible[i][x].remove(v)

    xs, ys = (x // 3) * 3, (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if v in possible[ys + i][xs + j]:
                possible[ys + i][xs + j].remove(v)

for y in range(9):
    line = input()
    for x in range(9):
        if line[x] != ".":
            add(x, y, int(line[x]))

changed = True
count = 0
while changed == True:
    valid_sudoku()

    changed = False
    for a in range(3):
        for b in range(3):
            block_possible = { i: 0 for i in range(1, 10) }
            for i in range(3):
                for j in range(3):
                    x = a * 3 + i
                    y = b * 3 + j

                    for p in possible[y][x]:
                        block_possible[p] += 1

            for k, c in block_possible.items():
                if c == 1:
                    for i in range(3):
                        for j in range(3):
                            x = a * 3 + i
                            y = b * 3 + j
                            if k in possible[y][x]:
                                add(x, y, k)
                                changed = True
                                count += 1

for line in table:
    print(*line, sep="")