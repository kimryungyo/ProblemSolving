n = int(input())
pens = input()
p1 = p2 = p3 = p4 = "N"

count = 0
i = 0
while True:
    if i >= len(pens): break
    pen = pens[i]
    p1, p2, p3 = p2, p3, p4
    p4 = pen

    if p1 + p2 + p3 + p4 == "pPAp":
        count += 1
        try:
            p1 = pens[i + 0]
            p2 = pens[i + 1]
            p3 = pens[i + 2]
            p4 = pens[i + 3]
            i += 3
        except: break

    i += 1

print(count)