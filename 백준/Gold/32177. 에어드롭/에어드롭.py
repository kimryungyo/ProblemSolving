def main():
    from collections import deque
    from sys import stdin
    input = lambda: stdin.readline().rstrip()

    N, K, T = map(int, input().split())
    X, Y, V = map(int, input().split())
    K = K ** 2

    graph = [ [] for _ in range(N) ]
    photos = [ None ] * N


    frineds = [ tuple(map(int, input().split())) for _ in range(N) ]
    photos[N - 1] = bool(frineds[N - 1][3])

    for i in range(N - 1):
        x1, y1, v1, p1 = frineds[i]
        photos[i] = bool(p1)

        for j in range(i + 1, N):
            x2, y2, v2, p2 = frineds[j]
            
            distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
            version = abs(v2 - v1)
            if distance <= K and version <= T:
                graph[i].append(j)
                graph[j].append(i)

    queue = deque()
    visited = [ False ] * N

    for i in range(N):
        x, y, v, p = frineds[i]
        distance = (X - x) ** 2 + (Y - y) ** 2
        version = abs(V - v)
        if distance <= K and version <= T:
            queue.append(i)
            visited[i] = True

    received = []

    while queue:
        node = queue.popleft()
        if photos[node]: received.append(node + 1)

        for next in graph[node]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True

    received.sort()
    if received: print(" ".join(map(str, received)))
    else: print(0)

if __name__ == "__main__":
    main()