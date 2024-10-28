def solution(N):
    num = 1
    length = 1

    while True:
        if num % N == 0: return length
        num = num * 10 + 1
        length += 1

for N in map(int, open(0)):
    print(solution(N))