from sys import stdin
input = lambda: stdin.readline().rstrip()

MOD = 10 ** 9 + 7

def solve_arithmetic_restoration(A, B, C):
    L = len(A)
    A = A[::-1]
    B = B[::-1]
    C = C[::-1]

    dp = [ [0] * 2 for _ in range(L + 1) ]
    dp[0][0] = 1

    for i in range(L):
        for carry_in in range(2):
            ways = dp[i][carry_in]
            if ways == 0:
                continue

            possible_a = get_possible_digits(A[i], is_leading=(i == L-1))
            possible_b = get_possible_digits(B[i], is_leading=(i == L-1))
            possible_c = get_possible_digits(C[i], is_leading=(i == L-1))

            for a in possible_a:
                for b in possible_b:
                    s = a + b + carry_in
                    c_expected = s % 10
                    carry_out = s // 10

                    if carry_out > 1:
                        continue

                    if c_expected in possible_c:
                        dp[i+1][carry_out] = (dp[i+1][carry_out] + ways) % MOD

    return dp[L][0] % MOD

def get_possible_digits(ch, is_leading=False):
    if ch == '?':
        if is_leading:
            return list(range(1, 10))
        else:
            return list(range(0, 10))
    else:
        digit = int(ch)
        if is_leading and digit == 0:
            return []
        return [digit]

def main():
    while True:
        A = input()
        if A == '0':  break
        B, C = input(), input()
        answer = solve_arithmetic_restoration(A, B, C)
        print(answer)

main()