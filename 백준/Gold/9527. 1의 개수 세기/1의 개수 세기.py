dp = [1]
for i in range(64): dp.append(dp[-1] * 2 + 2 ** i - 1)

def split_into_two_powers(number):
    powers = []
    while number > 0:
        power = 1
        for p in range(0, int(1e100)):
            power *= 2
            if power > number: break
        power //= 2
        number -= power
        powers.append(p)
    return powers

def get_one_count(number):
    count = 0
    powers = split_into_two_powers(number)
    for idx in range(len(powers)):
        power = powers[idx]
        count += dp[power]
        count += idx * (2 ** power)
    return count

a, b = map(int, input().split())
a_count = get_one_count(a - 1)
b_count = get_one_count(b)

print(b_count - a_count)