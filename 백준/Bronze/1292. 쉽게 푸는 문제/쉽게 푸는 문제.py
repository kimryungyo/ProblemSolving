add = 1
stack = 0

array = []
for i in range(1000):
    array.append(add)
    stack += 1
    if stack == add:
        add += 1
        stack = 0

a, b = map(int, input().split())
print(sum(array[a - 1: b]))