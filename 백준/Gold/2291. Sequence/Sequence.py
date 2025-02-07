N, M, K = map(int, input().split())

memo = {}
def get_candidates(slots, remains, minimum):

    if slots == 0:
        return 1 if remains == 0 else 0
    
    if remains < slots * minimum:
        return 0
    
    if (slots, remains, minimum) in memo:
        return memo[(slots, remains, minimum)]
    
    count = 0
    for candidate in range(minimum, remains+1):
        count += get_candidates(slots-1, remains-candidate, candidate)

    memo[(slots, remains, minimum)] = count
    return count

sequence = []
minimum = 1
remains = M
slots = N

for i in range(N):
    for candidate in range(minimum, remains+1):
        cnt = get_candidates(slots-1, remains-candidate, candidate)
        if K > cnt:
            K -= cnt
        else:
            sequence.append(candidate)
            remains -= candidate
            minimum = candidate
            slots -= 1
            break

print(" ".join(map(str, sequence)))