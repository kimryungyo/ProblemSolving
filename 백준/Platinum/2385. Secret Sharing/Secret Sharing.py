from collections import deque

def get_max_fragment_len(candidates):
    max_len = 0
    for key, used in candidates:
        for frag in numbers.keys():
            if numbers[frag] - used.get(frag, 0):
                if len(frag) > max_len:
                    max_len = len(frag)
    return max_len

def get_next_candidates(candidates):
    global now_len

    now_len += get_max_fragment_len(candidates)

    candi_to_tuple = lambda candi: ( candi[0], tuple(sorted(candi[1].items())) )

    next_candidates = []
    queue = deque(candidates)
    visited = { candi_to_tuple(candi) for candi in candidates }

    while queue:
        candidate = queue.popleft()
        key, used = candidate

        if len(key) >= now_len:
            next_candidates.append((key, used))
            continue

        for frag in numbers.keys():
            can_use = numbers[frag] - used.get(frag, 0)
            if can_use:
                new_used = used.copy()
                if frag not in new_used: new_used[frag] = 0
                new_used[frag] += 1

                next_candidate = (key + frag, new_used)
                tuple_candidate = candi_to_tuple(next_candidate)
                if tuple_candidate not in visited:
                    queue.append(next_candidate)
                    visited.add(tuple_candidate)

    return next_candidates

def get_used_candidates(candidates):
    global now_len

    next_candidates = get_next_candidates(candidates)

    min_weight = float("inf")
    used_candidates = []

    for key, used in next_candidates:

        new_num = key + "0" * (key_len - len(key))
        if new_num[0] == "0": continue
        new_num = int(new_num)
        new_weight = int(key[:now_len])

        if new_weight < min_weight:
            min_weight = new_weight
            used_candidates = [(key, used)]
        elif new_weight == min_weight:
            used_candidates.append((key, used))

    return used_candidates

N = int(input())
nums = input().split()
key_len = sum(len(num) for num in nums)
now_len = 0

if all(num[0] == "0" for num in nums):
    print("INVALID")
    quit()

numbers = {}
for num in nums:
    if num not in numbers:
        numbers[num] = 0
    numbers[num] += 1

used_candidates = [ ("", {}) ]
while True:
    used_candidates = get_used_candidates(used_candidates)
    key_candidates = { key for key, used in used_candidates }
    
    if len(key_candidates) == 1:
        key_candidate = key_candidates.pop()
        if len(key_candidate) == key_len:
            print(key_candidate)
            break