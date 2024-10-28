from math import gcd
from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
A = 1
for num in map(int, input().split()):
    A *= num

m = int(input())
B = 1
for num in map(int, input().split()):
    B *= num

print(str(gcd(A, B))[-9:])