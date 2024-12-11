T = int(input())
for _ in range(T):
    cards = map(int, input().split())
    nums = []
    for idx, count in enumerate(cards):
        num = idx + 1 if idx != 5 else 9
        nums.extend([num] * count)
    nums.sort()

    pos = False
    left, right = 0, -1

    answer = [ 0 ] * len(nums)
    while nums:
        num = nums.pop()

        if not pos:
            answer[left] = num
            left += 1
        else:
            answer[right] = num
            right -= 1
        pos = not pos

    print(" ".join(map(str, answer)))