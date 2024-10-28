mi, mv = 0, 0
for i in range(1, 10):
    v = int(input())
    if v > mv:
        mi = i
        mv = v
print(mv)
print(mi)