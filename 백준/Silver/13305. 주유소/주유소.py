N = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))
prices[N - 1] = -1

before_price = prices[0]
stations = [ ]
distance = 0
for i in range(1, N):
    price = prices[i]
    distance += roads[i - 1]

    if price < before_price:
        stations.append((distance, price))
        before_price = price
        distance = 0

oil_price = prices[0]
paid = 0
for dist, price in stations:
    paid += dist * oil_price
    oil_price = price
print(paid)