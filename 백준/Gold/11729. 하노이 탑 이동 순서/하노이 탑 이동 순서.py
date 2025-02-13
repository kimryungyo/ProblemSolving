def hanoi(n, start, end, moves):
    if n == 1:
        moves.append((start, end))
    else:
        aux = 6 - start - end
        hanoi(n - 1, start, aux, moves)
        moves.append((start, end))
        hanoi(n - 1, aux, end, moves)

def print_answer(moves):
    from sys import stdout
    stdout.write(f"{len(moves)}\n")
    stdout.write("\n".join(f"{a} {b}" for a, b in moves))

n = int(input().strip())
moves = []
hanoi(n, 1, 3, moves)
print_answer(moves)