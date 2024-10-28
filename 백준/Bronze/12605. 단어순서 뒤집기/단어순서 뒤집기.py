N, *strings = open(0).read().split("\n")
for i in range(int(N)): print(f'Case #{i+1}: '+' '.join(strings[i].split()[::-1]))