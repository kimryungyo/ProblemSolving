from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    N, string = input().split()
    N = int(N)
    
    for char in string:
        print(char * N, end="")
    print()