from sys import setrecursionlimit
setrecursionlimit(10 ** 4)

N, *works = map(int, open(0).read().split())

counts = [0] * 7
for work in works:
    counts[work % 7] += 1


visited = [ [-1] * 7 for _ in range(7) ]

def dfs(sum):
    lower = True
    for count, vis_count in zip(counts, visited[sum % 7]):
        if count > vis_count: 
            lower = False
    if lower: return None

    visited[sum % 7] = list(counts)

    if sum % 7 == 4:
        print("YES")
        quit()

    for add in range(7):
        if counts[add]:
            next = sum + add
            counts[add] -= 1
            dfs(next)
            counts[add] += 1

dfs(0)
print("NO")