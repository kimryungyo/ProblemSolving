Y = int(input())
if Y % 4 == 0:
    if Y % 400 == 0: print(1)
    elif Y % 100 == 0: print(0)
    else: print(1)
else: print(0)