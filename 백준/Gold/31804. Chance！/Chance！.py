from collections import deque

a, b = map(int, input().split())

queue = deque([(a, 0, False)])

visited_1 = [float("inf")] * 1000001
visited_2 = [float("inf")] * 1000001

while queue:
    current, count, chance = queue.popleft()

    if current == b: print(count); quit()
    next_count = count + 1

    if current + 1 <= b:
        if chance is False:
            if visited_1[current + 1] > next_count:
                queue.append((current + 1, next_count, chance))
                visited_1[current + 1] = next_count

        elif visited_2[current + 1] > next_count:
            queue.append((current + 1, next_count, chance))
            visited_2[current + 1] = next_count

    if current * 2 <= b:
        if chance is False:
            if visited_1[current * 2] > next_count:
                queue.append((current * 2, next_count, chance))
                visited_1[current * 2] = next_count

        elif visited_2[current * 2] > next_count:
            queue.append((current * 2, next_count, chance))
            visited_2[current * 2] = next_count

    if current * 10 <= b:
        if chance is False:
            if visited_1[current * 10] > next_count:
                queue.append((current * 10, next_count, True))
                visited_2[current * 10] = next_count