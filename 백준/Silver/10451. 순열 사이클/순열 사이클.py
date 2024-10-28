T = int(input())

for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0

    graph = {}
    for i in range(1, n + 1):
        graph[i] = nums[i - 1]

    visiting = { i for i in range(1, n + 1) }
    while visiting:
        root = visiting.pop()
        visiting.add(root)
        now = root

        while now in graph:
            now = graph[now]
            visiting.remove(now)
            if now == root: break

        count += 1

    print(count)