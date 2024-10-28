n = int(input())
for _ in range(n):
    result = 0
    for number in range(int(input())):
        result += number // 2
    print(result)