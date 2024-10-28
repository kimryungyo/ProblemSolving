from sys import stdin
input = lambda: stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    n = int(input())
    scores = [ tuple(map(int, input().split())) for _ in range(n) ]
    scores.sort(key=lambda x: x[0])
    
    count = 1
    min_talk = scores[0][1]
    
    for i in range(1, n):
        if scores[i][1] < min_talk:
            count += 1
            min_talk = scores[i][1]

    print(count)