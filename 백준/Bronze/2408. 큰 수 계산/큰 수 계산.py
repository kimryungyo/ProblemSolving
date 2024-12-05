N, *exp = open(0)
exp = "".join(exp).replace("\n", "").replace("/", "//")
print(eval(exp))