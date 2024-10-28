from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
scores = list(map(int, input().split()))

max_num, max_score = -1, -1
for _ in range(M):
    num, *grading = input().split()
    num = int(num)
    score = sum( scores[i] for i in range(N) if grading[i] == "O" )

    if score > max_score:
        max_num, max_score = num, score

    elif score == max_score and num < max_num:
        max_num = num

print(max_num, max_score)