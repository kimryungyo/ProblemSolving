from random import randint
from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    max_mul = 10 ** 18 // N

    while True:
        num = randint(1, max_mul) * N
        if sum(int(n) for n in str(num)) % 2 == 1:
            print(num)
            break