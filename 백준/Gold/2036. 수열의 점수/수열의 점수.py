def main(nums):
    plus = []
    ones = 0
    zeros = 0
    minus = []

    for num in nums:
        if num > 1:
            plus.append(num)
        elif num == 1:
            ones += 1
        elif num == 0:
            zeros += 1
        else:
            minus.append(num)

    plus.sort(reverse=True)
    minus.sort()
    score = 0

    i = 0
    while i < len(plus):
        if i + 1 < len(plus):
            score += plus[i] * plus[i+1]
            i += 2
        else:
            score += plus[i]
            i += 1

    score += ones

    i = 0
    while i < len(minus):
        if i + 1 < len(minus):
            score += minus[i] * minus[i+1]
            i += 2
        else:
            if zeros == 0:
                score += minus[i]
            i += 1

    return score

N, *nums = map(int, open(0))
print(main(nums))