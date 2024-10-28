from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
nums = list(map(int, input().split()))

min_dist = float('inf')
min_k = None

sums = [0]
sum_ = 0
for num in nums:
    sum_ += num
    sums.append(sum_)

def range_sum(i, k):
    sum_ = sums[i + k] - sums[i]
    return sum_

k_max = n // 2
range_sums = { k: set() for k in range(k_max + 1) }
for k in range(1, k_max + 1):
    range_sums[k].add( ( 0, range_sum(0, k) ) )

    for i in range(len(nums) - k + 1):
        sum_ = range_sum(i, k)
        range_sums[k].add( ( i, sum_ ) )

keys = list(range_sums.keys())
keys.reverse()

for k in keys:
    k_sums = range_sums[k]
    k_sums = sorted(k_sums, key=lambda x: x[1])

    for a in range(len(k_sums) - 1):
        for b in range(a + 1, len(k_sums)):
            i, i_sum = k_sums[a]
            j, j_sum = k_sums[b]

            if abs(j - i) < k: continue

            dist = abs(i_sum - j_sum)
            if dist >= min_dist: break

            if dist < min_dist:
                min_dist = dist
                min_k = k

            elif dist == min_dist:
                min_k = k

            break

print(min_k)
print(min_dist)
