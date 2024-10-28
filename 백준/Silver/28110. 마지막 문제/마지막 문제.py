N, *D = map(int, open(0).read().split())
D.sort()

min = 0
res = -1

bef = D[0]
for diff in D:
  dist = (diff - bef) // 2

  if dist > min:
    min = dist
    res = bef + dist

  bef = diff

print(res)