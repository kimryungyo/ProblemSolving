n, *words = open(0).read().split()

orders = {}
for word in words:
    length = len(word)
    if length not in orders: orders[length] = set()
    orders[length].add(word)

for length in sorted(orders.keys()):
    orders[length] = sorted(orders[length])
    print("\n".join(orders[length]))