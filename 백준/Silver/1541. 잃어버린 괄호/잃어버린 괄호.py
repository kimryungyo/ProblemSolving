exp = input()

if "-" not in exp:
    if "+" not in exp: print(exp)
    else: print(sum(map(int, exp.split("+"))))
    quit()

res = 0
plus, minus = exp.split("-", 1)

plus = plus.replace("+", " ")
res += sum(map(int, plus.split()))

minus = minus.replace("-", " ").replace("+", " ")
res -= sum(map(int, minus.split()))

print(res)