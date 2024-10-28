from sys import stdin, setrecursionlimit
input = lambda: stdin.readline().rstrip()
setrecursionlimit(10 ** 6)

def dfs(number):
    visited[number] = True
    dp[number][0] = 0
    dp[number][1] = 1

    for child in graph[number]:
        if not visited[child]:
            dfs(child)
            dp[number][0] += dp[child][1]
            dp[number][1] += min(dp[child][0], dp[child][1])

n = int(input())
dp = [ [0, 0] for _ in range(n + 1) ]
visited = [False] * (n + 1)
graph = [ [] for _ in range(n + 1) ]

for i in range(1, n):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

dfs(1)
print(min(dp[1][0], dp[1][1]))