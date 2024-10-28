from sys import stdin
input = lambda: stdin.readline().rstrip()

cache = [None] * 16
cache[0] = r"{}"
memo = {r"{}": 0}

def caching(n, cache = cache, memo = memo):
 if cache[n]: return cache[n]
 d=[ caching(i) for i in range(n) ]
 set = f"{{{','.join(d)}}}"
 cache[n] = set
 memo[set] = n
 return set

caching(15)

T = int(input())
for _ in range(T):
 C = memo[input()] + memo[input()]
 print(cache[C])