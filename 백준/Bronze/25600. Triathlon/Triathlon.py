from sys import stdin
input = lambda: stdin.readline().rstrip()

def calculate_score(a, d, g):
    if a == d + g: return 2 * a * (d + g)
    else: return a * (d + g)

N = int(input())
max_score = 0

for _ in range(N):
    a, d, g = map(int, input().split())
    score = calculate_score(a, d, g)
    max_score = max(max_score, score)

print(max_score)