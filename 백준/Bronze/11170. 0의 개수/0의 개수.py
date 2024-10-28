t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    zero_count = 0
    for num in range(n, m + 1):
        zero_count += str(num).count("0")

    print(zero_count)