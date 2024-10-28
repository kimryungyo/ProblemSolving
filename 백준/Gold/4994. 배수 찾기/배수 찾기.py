from collections import deque

def bfs(n):
    queue = deque()
    queue.append("1")

    while queue:
        num = queue.popleft()
        remainder = int(num) % n
        if remainder == 0: return num
        else:
            queue.append(num + "0") 
            queue.append(num + "1")

while True:
    n = int(input())
    if n == 0:  break
    result = bfs(n)
    print(result)