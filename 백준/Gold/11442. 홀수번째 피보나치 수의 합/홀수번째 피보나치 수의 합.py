MOD = 1000000007

class Matrix:
    """2x2 행렬을 저장하는 클래스"""

    def __init__(self, matrix):
        self.matrix = matrix

    def __mul__(self, other: "Matrix"):
        """2x2 행렬의 곱을 반환하는 함수"""
        a, b = self, other
        return Matrix([
            [ (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % MOD, (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % MOD ],
            [ (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % MOD, (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % MOD ]
        ])

    def __pow__(self, n):
        """분할 정복 거듭제곱을 이용해 행렬의 n제곱을 구하는 함수"""
        result = Matrix([[1, 0], [0, 1]])
        base = self
        while n:
            if n & 1:
                result = result * base
            base = base * base
            n //= 2
        return result

    def __getitem__(self, idx):
        return self.matrix[idx]

def fibo(n):
    """행렬의 거듭제곱을 이용해 n번째 피보나치 수를 구하는 함수"""
    if n < 2:
        return n
    matrix = Matrix([[1, 1], [1, 0]])
    result = matrix ** (n - 1)
    return result[0][0]

N = int(input())
answer = fibo(N) if N % 2 == 0 else fibo(N + 1)
print(answer)