from sys import stdin
input = lambda: stdin.readline().rstrip()

N = int(input())

for _ in range(N):
    command = input()
    
    if command.startswith("Simon says"):
        print(command.replace("Simon says", ""))