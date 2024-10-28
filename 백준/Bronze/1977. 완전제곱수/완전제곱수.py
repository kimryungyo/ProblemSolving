import math
M = int(input().strip())
N = int(input().strip())

perfect_squares = []

for i in range(math.ceil(math.sqrt(M)), math.floor(math.sqrt(N)) + 1):
    square = i * i
    if M <= square <= N:
        perfect_squares.append(square)

if perfect_squares:
    print(sum(perfect_squares))
    print(min(perfect_squares))
else:
    print(-1)