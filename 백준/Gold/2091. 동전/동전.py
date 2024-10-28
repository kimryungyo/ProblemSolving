from math import ceil
x, c, n, d, q = map(int, input().split())

cm = c
nm = n * 5 + cm
dm = d * 10 + nm

case = (0, 0, 0, 0)
max_count = 0

if x > dm: qs = ceil((x - dm) / 25)
else: qs = 0

for qua in range(qs, q + 1):
    price_1 = qua * 25
    if price_1 > x: break

    if (x - price_1) > nm: ds = ceil((x - price_1 - nm) / 10)
    else: ds = 0

    for dim in range(ds, d + 1):
        price_2 = price_1 + dim * 10
        if price_2 > x: break

        if (x - price_2) > cm: ns = ceil((x - price_2 - cm) / 5)
        else: ns = 0

        for nic in range(ns, n + 1):
            price_3 = price_2 + nic * 5
            if price_3 > x: break

            cen = x - price_3
            if cen <= c:
                count = cen + nic + dim + qua 
                if count > max_count:
                    max_count = count
                    case = (cen, nic, dim, qua)
                
print(*case)