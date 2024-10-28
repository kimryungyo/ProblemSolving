from collections import deque
n, *mountains = map(int, open(0).read().split())
mountains = deque(mountains)

total_price = 0
before = mountains.popleft()

while mountains:
    now = mountains.popleft()
    distance = now + before
    height = abs(now - before)
    price = distance ** 2 + height ** 2
    total_price += price
    before = now

print(total_price)