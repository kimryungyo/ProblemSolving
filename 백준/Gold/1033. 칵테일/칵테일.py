from fractions import Fraction
from math import lcm

n = int(input())

links = { i: [] for i in range(n) }
ratios = { i: { i : Fraction(1) } for i in range(n) }

for _ in range(n-1):
    a, b, p, q = map(int, input().split())
    links[a].append(b)
    links[b].append(a)
    ratios[a][b] = Fraction(q, p)
    ratios[b][a] = Fraction(p, q)

def get_ratio(b):

    def find_path(graph, target, current=0, path=[]):
        path = path + [current]
        
        if current == target:
            return path
        
        for neighbor in graph[current]:
            if neighbor not in path:
                new_path = find_path(graph, target, neighbor, path)
                if new_path:
                    return new_path
        
        return None
                
    path = find_path(ratios, b)
    ratio = Fraction(1)

    for i in range(1, len(path)):
        ratio *= ratios[path[i-1]][path[i]]

    return ratio

results = []
denominators = []

for i in range(n):
    ratio = get_ratio(i)
    results.append(ratio)
    denominators.append(results[i].denominator)

mass = lcm(*denominators)
print(*[ mass * results[i] for i in range(n) ])