from sys import stdin
input = lambda: stdin.readline().rstrip()

N = int(input())
participants = []

for _ in range(N):
    problems, penalty = map(int, input().split())
    participants.append((problems, penalty))

participants.sort(key=lambda x: (-x[0], x[1]))

fifth_place_problems = participants[4][0]

count = 0
for i in range(5, N):
    if participants[i][0] == fifth_place_problems:
        count += 1
    else: break

print(count)