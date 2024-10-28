import itertools as i
print("\n".join(" ".join(p)for p in i.permutations(map(str,range(1,int(input())+1)))))