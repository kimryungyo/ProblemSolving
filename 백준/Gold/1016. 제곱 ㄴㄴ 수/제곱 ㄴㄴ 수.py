from math import ceil, floor

def sieve_of_eratosthenes(limit):
    prime_flags = [True] * (limit+1)
    prime_flags[0] = prime_flags[1] = False
    for num in range(2, int(limit**0.5)+1):
        if prime_flags[num]:
            for multiple in range(num*num, limit+1, num):
                prime_flags[multiple] = False
    primes_list = [num for num in range(2, limit+1) if prime_flags[num]]
    return primes_list

def main(min_val = None, max_val = None):
    if min_val == None or max_val == None: min_val, max_val = map(int, input().split())

    numbers_list = [True] * (max_val - min_val + 1)
    primes_list = sieve_of_eratosthenes(int(max_val ** 0.5))
    for prime_num in primes_list:
        min_quotient = ceil(min_val / prime_num ** 2)
        max_quotient = floor(max_val / prime_num ** 2)

        for multiplier in range(min_quotient, max_quotient + 1): numbers_list[multiplier * (prime_num ** 2) - min_val] = False

    print(numbers_list.count(True))

main()

