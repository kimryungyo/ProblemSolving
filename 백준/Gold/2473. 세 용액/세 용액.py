n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

minimum = float('inf')
minimum_items = [None, None, None]

def find_closest_element(range_, target):
    left, right = range_
    
    if target <= solutions[left]:
        return solutions[left]
    if target >= solutions[right]:
        return solutions[right]
    
    while left <= right:
        mid = (left + right) // 2
        
        if solutions[mid] == target:
            return solutions[mid]
        elif solutions[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    if left >= len(solutions):
        return solutions[right]
    if right < 0:
        return solutions[left]
    
    if abs(solutions[left] - target) < abs(solutions[right] - target):
        return solutions[left]
    else:
        return solutions[right]

for i in range(len(solutions) - 2):
    for j in range(i + 1, len(solutions) - 1):
        range_ = j + 1, len(solutions) - 1
        target = (solutions[i] + solutions[j]) * -1
        last_value = find_closest_element( (j + 1, len(solutions) - 1) , target)
        sum_ = solutions[i] + solutions[j] + last_value
        if abs(sum_) < minimum:
            minimum = abs(sum_)
            minimum_items = [solutions[i], solutions[j], last_value]

print(*minimum_items)