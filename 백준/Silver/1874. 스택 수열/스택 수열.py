from sys import stdin
input = lambda: stdin.readline().rstrip()

from collections import deque

n = int(input())
sequence = deque([ int(input()) for _ in range(n) ])

nums = deque([ num for num in range(1, n + 1) ])
stack = []

operations = []
while nums or stack:
    if stack and stack[-1] == sequence[0]:
        sequence.popleft()
        stack.pop()
        operations.append("-")

    else:
        if not nums: print("NO"); quit()
        number = nums.popleft()
        stack.append(number)
        operations.append("+")

print("\n".join(operations))