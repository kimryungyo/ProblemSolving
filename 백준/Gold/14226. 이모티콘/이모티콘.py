from collections import deque
N = int(input())
visited = [ [ False ] * (N + 1) for _ in range(N * 2 + 1) ]
visited[1][0] = 0

queue = deque([ (1, 0) ])
while queue:
    count, clipboard = queue.popleft()

    if count == N:
        print(visited[count][clipboard])
        quit()

    time = visited[count][clipboard] + 1

    if count < N:
        if visited[count][count] is False:
                visited[count][count] = time
                next = (count, count)
                queue.append(next)

    if count < N:
        if visited[count + clipboard][clipboard] is False:
            visited[count + clipboard][clipboard] = time
            next = (count + clipboard, clipboard)
            queue.append(next)

    if count > 1:
        if visited[count - 1][clipboard] is False:
            visited[count - 1][clipboard] = time
            next = (count - 1, clipboard)
            queue.append(next)