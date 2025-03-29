def compute_score(values, k):
    score = 0
    max_score = 0
    for i, value in enumerate(values[:min(len(values), k)]):
        max_score = max(max_score, score + (k - i) * value)
        score += value
    return max_score

n, k = map(int, input().split())
arr = list(map(int, input().split()))

score_clock = compute_score(arr, k)
score_counter = compute_score(arr[::-1], k)

print(max(score_clock, score_counter))