from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
names = [ input() for _ in range(n) ]
sorts = sorted(names, reverse=True)

if names == list(reversed(sorts)):
    print("INCREASING")

elif names == sorts:
    print("DECREASING")

else:
    print("NEITHER")