from math import gcd
A, B = map(int, input().split())
print("1" * gcd(A, B))