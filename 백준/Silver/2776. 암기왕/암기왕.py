from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    N = input()
    note_1 = set(input().split())

    M = input()
    note_2 = input().split()

    for num in note_2:
        print(int(num in note_1))