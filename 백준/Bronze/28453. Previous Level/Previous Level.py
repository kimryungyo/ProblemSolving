n = int(input())
levels = list(map(int, input().split()))
for level in levels:
    if level >= 300: print(1, end=' ')
    elif level >= 275: print(2, end=' ')
    elif level >= 250: print(3, end=' ')
    else: print(4, end=' ')