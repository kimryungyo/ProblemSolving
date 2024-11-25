N, M = map(int, input().split())
count = 0

bundles = N
while bundles >= M:
    count += bundles
    bundles //= M
count += bundles

print(count)