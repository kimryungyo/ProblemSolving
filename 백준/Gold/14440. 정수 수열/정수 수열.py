def matmul(A, B):
    return [[(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % 100,
              (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % 100],
             [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % 100,
              (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % 100]]

def matpow(M, n):
    result = [[1, 0],
              [0, 1]]
    
    base = M
    while n > 0:
        if n % 2 == 1:
            result = matmul(result, base)
        base = matmul(base, base)
        n //= 2
    
    return result

x, y, a0, a1, n = map(int, input().split())
x %= 100
y %= 100

if n == 0:
    print(f"{a0:02d}")
    quit()

if n == 1:
    print(f"{a1:02d}")
    quit()

M = [[x, y],
     [1, 0]]

Mn_1 = matpow(M, n-1)

An = (Mn_1[0][0] * a1 + Mn_1[0][1] * a0) % 100

print(f"{An:02d}")