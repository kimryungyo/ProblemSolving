def hanoi(n, start, end, moves):
    if n == 1:
        moves.append((start, end))
    else:
        aux = 6 - start - end
        hanoi(n - 1, start, aux, moves)
        moves.append((start, end))
        hanoi(n - 1, aux, end, moves)

n = int(input().strip())
moves = []
hanoi(n, 1, 3, moves)
print(len(moves))
print("\n".join(f"{a} {b}" for a, b in moves))