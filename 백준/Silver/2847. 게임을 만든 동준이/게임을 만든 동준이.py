from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
stages = [ int(input()) for _ in range(n) ]

before = float("inf")
total = 0
while stages:
    score = stages.pop()
    if score >= before:
        remove = score - before + 1
        score -= remove
        total += remove
    before = score

print(total)