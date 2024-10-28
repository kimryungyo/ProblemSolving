n = int(input())
buildings = list(map(int, input().split()))

from fractions import Fraction

def see(position, arr):
    count = 0
    max_radian = None
    dx = 0
    for height in arr:
        dx += 1
        dy = height - position
        radian = Fraction(dy, dx)

        if max_radian is None: 
            count += 1
            max_radian = radian

        else:
            if radian > max_radian:
                count += 1
                max_radian = radian

    return count

def check(n):
    position = buildings[n]
    lefts = buildings[:n][::-1]
    rights = buildings[n + 1:]

    count = 0
    count += see(position, lefts)
    count += see(position, rights)
    return count

max_count = 0
for i in range(len(buildings)):
    count = check(i)
    if count > max_count:
        max_count = count

print(max_count) 