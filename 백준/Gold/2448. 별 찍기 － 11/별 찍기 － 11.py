from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
input = lambda: stdin.readline().rstrip()

def draw_stars(n):
    if n == 3: return ['  *  ', ' * * ', '*****']
    
    stars = draw_stars(n // 2)
    result = []
    
    for s in stars: result.append(' ' * (n // 2) + s + ' ' * (n // 2))
    for s in stars: result.append(s + ' ' + s)
    
    return result

n = int(input())
pattern = draw_stars(n)
for line in pattern: print(line)