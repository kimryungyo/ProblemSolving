from sys import stdin
input = lambda: stdin.readline().rstrip()

def find_closest_element(arr, target):
    left, right = 0, len(arr) - 1
    if target <= arr[left]:
        return arr[left]
    if target >= arr[right]:
        return arr[right]
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    if left >= len(arr):
        return arr[right]
    if right < 0:
        return arr[left]
    
    if abs(arr[left] - target) < abs(arr[right] - target):
        return arr[left]
    else:
        return arr[right]

tc = int(input())

for _ in range(tc):

    k, n = map(int, input().split())

    count = 0

    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    C = set(map(int, input().split()))
    D = set(map(int, input().split()))

    ab_sums = set()
    for a in A:
        for b in B:
            sum_ = a + b
            ab_sums.add(sum_)

    cd_sums = set()
    for c in C:
        for d in D:
            sum_ = c + d
            cd_sums.add(sum_)

    cd_sums = list(cd_sums)
    cd_sums.sort()

    min_diff = float('inf')
    min_value = None

    for ab_sum in ab_sums:
        target = k - ab_sum
        last = find_closest_element(cd_sums, target)

        diff = abs(k - (ab_sum + last))
        
        if diff == min_diff:
            min_value = min(min_value, ab_sum + last)

        elif diff < min_diff:
            min_diff = diff
            min_value = ab_sum + last

    print(min_value)