N = int(input())
for i in range(N, 0, -1):
    for j in range(N, i, -1): print(" ", end="")
    for k in range(0, i): print("*", end="")
    print()