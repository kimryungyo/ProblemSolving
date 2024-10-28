def sieve_of_eratosthenes(limit):
    prime_flags = [True] * (limit+1)

    for num in range(2, int(limit**0.5)+1):
        if prime_flags[num]:
            for multiple in range(num*num, limit+1, num): prime_flags[multiple] = False

    return [i for i in range(2, limit+1) if prime_flags[i]]

def main():
    test_cases = int(input())

    for _ in range(test_cases):
        number = int(input())
        for prime_num in sieve_of_eratosthenes(number):
            count = 0
            while (number % prime_num == 0):
                number /= prime_num
                count += 1
            if count != 0: print(prime_num, count)

main()

