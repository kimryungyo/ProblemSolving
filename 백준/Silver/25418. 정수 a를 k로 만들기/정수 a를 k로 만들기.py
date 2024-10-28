from collections import deque
A, K = map(int, input().split())

queue = deque([A])
counts = {A: 0}

while queue:
    num = queue.popleft()
    if num > K: continue
    if num == K: break
    else:
        num_add = num + 1
        if num_add not in counts:
            queue.append(num_add)
            counts[num_add] = counts[num] + 1

        num_mul = num * 2
        if num_mul not in counts:
            queue.append(num_mul)
            counts[num_mul] = counts[num] + 1

print(counts[K])