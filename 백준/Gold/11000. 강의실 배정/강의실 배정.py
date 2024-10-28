from sys import stdin
input = lambda: stdin.readline().rstrip()

N = int(input())
classes = []

for _ in range(N):
    s, e = map(int, input().split())
    classes.append( (s, True) )
    classes.append( (e, False) )

classes.sort()

active = 0
max_active = 0
for pos, type in classes:
    if type is True: active += 1
    else: active -= 1
    if active > max_active: 
        max_active = active

print(max_active)