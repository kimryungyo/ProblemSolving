def count_valid_pairs(N, S, cow_lengths):
    cow_lengths.sort()
    
    left = 0
    right = N - 1
    count = 0
    
    while left < right:
        if cow_lengths[left] + cow_lengths[right] <= S:
            count += (right - left)
            left += 1
        else:
            right -= 1
    
    return count

n, s = map(int, input().split())
cow_lengths = [int(input()) for _ in range(n)]

result = count_valid_pairs(n, s, cow_lengths)

print(result)
