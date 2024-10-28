from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())

passwords = {}
for _ in range(N):
    site, password = input().split()
    passwords[site] = password

for _ in range(M):
    site = input()
    print(passwords[site])