from collections import Counter
def get_value(n):
    c = Counter(map(int, list(str(n))))
    total = 0
    for i, m in c.items(): total += (i ** k) * m
    return total

a, b, k = map(int, input().split())
s = {}

total = 0
checked = {}

mins = []
for n in range(a, b + 1):
    
    loop = {n: 0}

    t = n

    i = 0
    while (i := i + 1):
        next = get_value(t)

        if next in loop:
            minimum = min(loop)
            min_idx = loop[minimum]
            for val, idx in loop.items():
                if idx <= min_idx:
                    checked[val] = minimum

            total += minimum
            mins.append(minimum)
            break

        elif next in checked:
            minimum = min(min(loop), checked[next])

            min_idx = loop[minimum] if minimum != checked[next] else checked[next] + 1
            for val, idx in loop.items():
                if idx <= min_idx:
                    checked[val] = minimum

            total += minimum
            mins.append(minimum)
            break

        t = next
        loop[next] = i

print(total)