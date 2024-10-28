from math import floor, ceil
x, y, d, t = map(int, open(0).read().split())

length = (x ** 2 + y ** 2) ** 0.5

jumps = [floor(length / d), ceil(length / d)]
walks = [abs(length - jumps[0] * d), abs(length - jumps[1] * d)]

cases = []

# case 1
if jumps[0] > 0:
    time = (jumps[0] + 1) * t
    cases.append(time)

# case 2
if length <= d * 2:
    time = 2 * t
    cases.append(time)

# case 3
time = jumps[1] * t + walks[1]
cases.append(time)

# case 4 
time = jumps[0] * t + walks[0]
cases.append(time)

# case 5 
time = length
cases.append(time)

print(min(cases))