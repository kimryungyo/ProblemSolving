R, C, ZR, ZC = map(int, input().split())
lines = [ input() for _ in range(R) ]

for line in lines:
    for _ in range(ZR):
        for char in line:
            print(char * ZC, end="")
        print()