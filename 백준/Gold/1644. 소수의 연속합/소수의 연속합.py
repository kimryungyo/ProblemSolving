def find_primes(n: int) -> list:
    
    primes = [True] * (n+1)
    
    for i in range(2, (n // 2) + 1):
        if primes[i]:

            for j in range(i*i, n+1, i):
                primes[j] = False
    
    return [i for i in range(2, n+1) if primes[i]]



def main(number: int = None) -> int:

    if number == None: number = int(input())
    primes_list = find_primes(number)
    start_point, end_point = 0, 0
    count = 0

    while end_point < len(primes_list):

        num_sum = sum(primes_list[start_point:end_point+1])

        if num_sum == number:
            count += 1
            end_point += 1

        if num_sum > number: start_point += 1

        if num_sum < number: end_point += 1

    return count

print(main())
