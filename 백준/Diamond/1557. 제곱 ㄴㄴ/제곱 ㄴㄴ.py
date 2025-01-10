from bisect import bisect_left

def eratosthenes(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    
    return [ i for i in range(2, n + 1) if prime[i] ]

def multiply_combinations(A, B):
    result = []
    for a in A:
        for b in B:
            result.append(a * b)
    return result

class NonSquareNumber:
    def __len__(self):
        return scan_ranges
    
    def __getitem__(self, index):
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

                new_value = multiply_values[-2] * sqaures[new_index] 
                multiply_values[-1] = new_value

            else:
                new_index = multiply_indexs[-1] + 1
                if new_index >= len(sqaures):
                    multiply_indexs[-1] = None
                    continue

                multiply_indexs.append(new_index)

                new_value = multiply_values[-1] * sqaures[new_index]
                multiply_values.append(new_value)

                if new_value > index:
                    multiply_indexs[-1] = None

            last_value = multiply_values[-1]
            if last_value <= index:
                square_number_count += (index // last_value) * ( (-1) ** len(multiply_indexs) )

        return index - square_number_count

max_sqaure = 45000
scan_ranges = max_sqaure ** 2 - 1
sqaures = [ i ** 2 for i in eratosthenes(max_sqaure + 1) ]

K = int(input())
scanner = NonSquareNumber()
answer = bisect_left(scanner, K)
print(answer)