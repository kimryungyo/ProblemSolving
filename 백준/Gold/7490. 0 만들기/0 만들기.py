from itertools import product
from sys import stdin
input = lambda: stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    nums = [ str(num) for num in range(1, N + 1) ]
    operaters = [ "+", "-", " " ]

    cases = []

    for opers in product(*[operaters] * (N - 1)):
        string_eval = nums[0]
        string_exp = nums[0]
        for oper, num in zip(opers, nums[1:]):
            if oper != " ": string_eval += oper
            string_eval += num
            string_exp += oper
            string_exp += num

        value = eval(string_eval)
        if value == 0:
            cases.append(string_exp)

    cases.sort()
    print("\n".join(cases))
    print()