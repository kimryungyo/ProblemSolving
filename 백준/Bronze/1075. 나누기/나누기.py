N=int(input());F=int(input());N=N//100*100
while N % F != 0: N += 1
print(str(N)[-2:].zfill(2))