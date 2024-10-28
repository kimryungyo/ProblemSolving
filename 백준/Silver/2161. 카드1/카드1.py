from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
queue = deque([ str(i) for i in range(n, 0, -1)])

result = ""
while len(queue) > 1:
    discard = queue.pop()
    result += discard + " "
    under = queue.pop()
    queue.appendleft(under)

result += queue.pop()
print(result)