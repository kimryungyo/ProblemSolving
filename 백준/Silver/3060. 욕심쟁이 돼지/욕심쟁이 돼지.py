from sys import stdin
input = stdin.readline

match = [ None, [1, 2, 6, 4], [2, 1, 3, 5], [3, 2, 4, 6], [4, 5, 3, 1], [5, 6, 4, 2], [6, 1, 5, 3] ]

T = int(input())
for _ in range(T):
    N = int(input())
    
    history = list(map(int, input().split()))
    total = sum(history)
    
    day = 1
    
    while N >= total:
        next = [ sum(history[other - 1] for other in match[num]) for num in range(1, 7) ]
        total = sum(next)
        history = next
        day += 1
    
    print(day)