from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    commands = input()
    n = int(input())
    nums = deque(eval(input()))

    reversed = False
    error = False
    for command in commands:
        if command == "R":
            reversed = not reversed
        else:
            if not nums:
                error = True
                break
            if reversed:
                nums.pop()
            else:
                nums.popleft()
    
    if error:
        print("error")
    else:
        nums = list(nums)
        if reversed: nums.reverse()
        string = str(nums).replace(" ", "")
        print(string)