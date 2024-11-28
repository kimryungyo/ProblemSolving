from collections import deque

def minimum_time_to_front(N, a, b):
    queue = deque()
    queue.append((N, 0))
    visited = [False] * (N + 1)
    visited[N] = True
    
    while queue:
        current_people, time_elapsed = queue.popleft()
        
        if current_people == 0:
            return time_elapsed
        
        next_people_wait = current_people - 1
        if next_people_wait >= 0 and not visited[next_people_wait]:
            visited[next_people_wait] = True
            queue.append((next_people_wait, time_elapsed + 1))
        
        if a > 0:
            next_people_a = current_people - 1 - a
            if next_people_a >= 0 and not visited[next_people_a]:
                visited[next_people_a] = True
                queue.append((next_people_a, time_elapsed + 1))
        
        if b > 0:
            next_people_b = current_people - 1 - b
            if next_people_b >= 0 and not visited[next_people_b]:
                visited[next_people_b] = True
                queue.append((next_people_b, time_elapsed + 1))
    
    return -1

N, a, b = map(int, open(0).read().split())
result = minimum_time_to_front(N, a, b)
print(result)