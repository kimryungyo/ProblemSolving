N, K, *nums = map(int, open(0).read().split())

nums_by_len = [ [] for _ in range(20) ]
for num in nums:
    binary = list(bin(num)[2:][::-1])
    for pos in range(len(binary)):
        if binary[pos] == "1":
            nums_by_len[pos].append(num)
nums_by_len_set = [ set(nums_len) for nums_len in nums_by_len ]

max_length = -1
for length in range(19, -1, -1):
    if len(nums_by_len[length]) < K: continue
    max_length = length
    break
if max_length == -1:
    print(0)
    quit()

valids = nums_by_len[max_length]

powers = [0] * 20
powers[max_length] = 1

for length in range(max_length - 1, -1, -1):
    new_valids = []

    for num in valids:
        if num in nums_by_len_set[length]:
            new_valids.append(num)

    if len(new_valids) < K: continue
    valids = new_valids
    powers[length] = 1

max_power = sum(2 ** i * powers[i] for i in range(20))
print(max_power)