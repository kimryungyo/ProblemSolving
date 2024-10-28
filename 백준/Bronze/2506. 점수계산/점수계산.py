input()
print(sum([sum(range(1,d.count("1")+1)) for d in input().split("0")]))