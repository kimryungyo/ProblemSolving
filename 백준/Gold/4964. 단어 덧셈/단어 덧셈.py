from sys import stdin
input = lambda: stdin.readline().rstrip()

while True:
    N = int(input())
    if N == 0: break

    chars = set()
    non_zeros = [0] * 100

    def scan_num(num, sums, chars, non_zeros):
        chars |= set(map(ord, num))
        if len(num) > 1: non_zeros[ord(num[0])] = 1

        for power, char in enumerate(reversed(num)):
            sums[ord(char)] += 10 ** power


    sums = [0] * 100
    for _ in range(N - 1): scan_num(input(), sums, chars, non_zeros)

    anss = [0] * 100
    scan_num(input(), anss, chars, non_zeros)

    chars = list(chars)
    matchs = [-1] * len(chars)

    can_uses = set(range(10))

    def dfs(sum = 0, ans = 0, idx = 0):
        if idx == len(chars):
            return 1 if sum == ans else 0

        count = 0

        for use in list(can_uses):
            if use == 0 and non_zeros[chars[idx]]: continue
            matchs[idx] = use

            can_uses.remove(use)
            new_sum = sum + sums[chars[idx]] * use
            new_ans = ans + anss[chars[idx]] * use
            count += dfs(new_sum, new_ans, idx + 1)
            can_uses.add(use)

        return count

    count = dfs()
    print(count)