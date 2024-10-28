from heapq import heappush, heappop

checked = set()
hq = []
k, n = map(int, input().split())
primes = list(map(int, input().split()))

for prime in primes:
    heappush(hq, prime)

count = 0
while True:
    item = heappop(hq)
    if item in checked: continue
    count += 1
    checked.add(item)

    if count == n:
        print(item)
        quit()
        
    for prime in primes:
        heappush(hq, item * prime)