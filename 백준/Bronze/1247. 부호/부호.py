from sys import stdin
input = lambda: stdin.readline().rstrip()

def get_sign_sum(numbers):
    sum_numbers = sum(numbers)
    if sum_numbers == 0: return "0"
    elif sum_numbers > 0: return "+"
    else: return "-"

for _ in range(3):
    N = int(input())
    numbers = [int(input()) for _ in range(N)]
    result = get_sign_sum(numbers)
    print(result)