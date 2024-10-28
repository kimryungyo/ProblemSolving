from math import ceil
N, L = map(int, input().split())

def sum_of_ints(a, b):
    return (b*(b+1)//2) - ((a-1)*a//2)

for leng in range(L, 100 + 1):
    s = ceil(N / leng)

    for _ in range(leng):
        if s < 0: break
        if sum_of_ints(s, s + leng - 1) == N:
            for num in range(s, s + leng):
                print(num, end = " ")
            quit()
        s -= 1

print(-1)