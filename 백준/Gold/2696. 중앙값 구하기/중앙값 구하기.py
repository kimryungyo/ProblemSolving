from collections import deque
from bisect import insort_left
INPUTS = deque(map(int, open(0).read().split()))
input = INPUTS.popleft

for _ in range(input()):
    N = input()
    array = []
    print(int(N / 2 + 0.5), end = "")
    for i in range(N):
        insort_left(array, input())
        if i % 2 == 0:
            if i % 20 == 0: print()
            print(array[len(array) // 2], end = " ")
    print()