import sys
input = lambda: sys.stdin.readline()

N, M = map(int, input().split())
orders = [ int(input()) for _ in range(N) ]

pos = 0
for moved in range(1, M + 1):
    dice = int(input())
    pos += dice

    if pos >= N - 1:
        print(moved)
        quit()

    order = orders[pos]
    pos += order
    
    if pos >= N - 1:
        print(moved)
        quit()