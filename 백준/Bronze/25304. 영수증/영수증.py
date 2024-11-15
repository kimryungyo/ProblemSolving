from sys import stdin
input = stdin.readline

amount = int(input())
counts = int(input())
total = 0

for _ in range(counts):
    price, quantity = map(int, input().split())
    total += price * quantity

if amount == total:
    print("Yes")
else:
    print("No")