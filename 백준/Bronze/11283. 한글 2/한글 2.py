IC = 19
MV = 21
FC = 28

HSC = 44032
c = input()
uv = ord(c)

i = uv - HSC

ici = i // (MV * FC)
mvi = (i // FC) % MV
fci = i % FC

r = ici * MV * FC + mvi * FC + fci + 1
print(r)