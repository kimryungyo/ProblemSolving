N, M = map(int, input().split())

for i in range(N):
    start_num = i * M + 1
    end_num = (i + 1) * M

    numbers = [str(num) for num in range(start_num, end_num + 1)]

    print(' '.join(numbers))