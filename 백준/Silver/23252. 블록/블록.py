from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    x, y, z = map(int, input().split())
    if ((x + z) % 2 == 0) and x >= z:
        if (y % 2 == 1) and (x == 0): 
            print("No")
        else: print("Yes")
    else: print("No")