l = []
while True:
    c = int(input())
    if c == 0: break
    else: l.append(c)

max_ = max(l)
result = []
idx = 0
while len(result) < max_:
    idx += 1
    if not len(set(str(idx))) < len(str(idx)): result.append(idx)

for i in l: print(result[i - 1])