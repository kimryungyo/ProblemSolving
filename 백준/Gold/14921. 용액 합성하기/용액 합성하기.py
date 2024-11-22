from bisect import bisect_left
N = int(input())
liquids = list(map(int, input().split()))

min_value = float("inf")
for i in range(N):
    index = bisect_left(range(N), 0, key = lambda x: (liquids[x] + liquids[i]))
    left, mid, right = index - 1, index, index + 1

    if 0 <= left < N and left != i:
        value = liquids[left] + liquids[i]
        if abs(value) < abs(min_value): min_value = value
        
    if 0 <= mid < N and mid != i:
        value = liquids[mid] + liquids[i]
        if abs(value) < abs(min_value): min_value = value

    if 0 <= right < N and right != i:
        value = liquids[right] + liquids[i]
        if abs(value) < abs(min_value): min_value = value

print(min_value)