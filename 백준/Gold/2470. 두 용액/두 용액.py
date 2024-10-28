def find_closest_to_zero(n, arr):
    arr.sort()
    l, r = 0, n - 1
    
    min_sum = float('inf')
    result = (0, 0)
    
    while l < r:
        sum_ = arr[l] + arr[r]
        
        if abs(sum_) < abs(min_sum):
            min_sum = sum_
            result = (arr[l], arr[r])
        
        if sum_ < 0: l += 1
        else: r -= 1
    
    return result

n = int(input())
liquids = list(map(int, input().split()))
result = find_closest_to_zero(n, liquids)
print(result[0], result[1])