stack = []
exps = list(input())

depth = 1
count = 0
for i in range(1, len(exps)):
    bef_exp = exps[i-1]
    exp = exps[i]
    if exp == "(": depth += 1
    else:
        depth -= 1
        if bef_exp == "(": count += depth
        else: count += 1

print(count)