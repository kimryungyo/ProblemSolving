a = list(map(int, input().split()))
a.sort()
d = a[1] - a[0]
d2 = a[2] - a[1]
if d > d2: print(a[0] + d2)
elif d == d2: print(a[2] + d)
else: print(a[1] + d)