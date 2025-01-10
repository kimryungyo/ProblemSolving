from bisect import bisect_left

def eratosthenes(n):
    """
    n 이하의 수들 중 소수를 판별하는 함수 (에라토스테네스의 체)
    """
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    
    return [ i for i in range(2, n + 1) if prime[i] ]

class NonSquareNumberScanner:
    """
    K번째 비제곱수를 탐색하는 클래스
    """

    def __init__(self, max_sqaure):
        """
        초기화 메소드
        탐색 범위 및 소수 제곱수들을 계산한다
        """
        self.scan_ranges = max_sqaure ** 2 - 1
        self.sqaures = [ i ** 2 for i in eratosthenes(max_sqaure + 1) ]

    def query(self, k):
        """
        K번째 비제곱수를 찾는 메소드
        bisect 라이브러리를 이용해 이진 탐색을 진행한다
        """
        return bisect_left(self, k)

    def __len__(self):
        """
        이진 탐색 범위
        """
        return self.scan_ranges
    
    def __getitem__(self, index):
        """
        인덱스가 몇번째 비제곱수 후의 수인지 반환하는 메소드
        소수 제곱수들로 포함 배제의 원리를 활용해 계산한다
        조합을 구할 때는 itertools.combinations이 아닌 DFS를 이용해 불필요한 탐색을 방지한다
        """
        square_number_count = 0
        multiply_indexs = [ -1 ]
        multiply_values = [ 1 ]

        while True:
            if multiply_indexs[-1] is None:
                multiply_indexs.pop()
                multiply_values.pop()
                if len(multiply_indexs) == 1:
                    break

                new_index = multiply_indexs[-1] + 1
                multiply_indexs[-1] = new_index

                new_value = multiply_values[-2] * self.sqaures[new_index] 
                multiply_values[-1] = new_value

            else:
                new_index = multiply_indexs[-1] + 1
                if new_index >= len(self.sqaures):
                    multiply_indexs[-1] = None
                    continue

                multiply_indexs.append(new_index)

                new_value = multiply_values[-1] * self.sqaures[new_index]
                multiply_values.append(new_value)

                if new_value > index:
                    multiply_indexs[-1] = None

            last_value = multiply_values[-1]
            if last_value <= index:
                square_number_count += (index // last_value) * ( (-1) ** len(multiply_indexs) )

        return index - square_number_count

def solution():
    """
    풀이 함수
    """

    # 1,000,000,000번째 비제곱수를 찾기 위한 제곱수의 추측값
    # 정확히는 40,489 이지만 여유분을 두어 45,000으로 설정
    max_sqaure = 45000

    # 값 탐색
    k = int(input())
    scanner = NonSquareNumberScanner(max_sqaure)
    answer = scanner.query(k)

    # 정답 반환
    return answer

print(solution())
