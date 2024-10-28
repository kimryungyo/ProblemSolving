def generate_digit_counts(max_depth):
    counts = {}
    counts[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counts[1] = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

    current_count = counts[1]
    for depth in range(0, max_depth):

        add_one = 10 ** depth - 1
        add_default = depth * 10 ** (depth - 1) if depth != 0 else 0

        for num in range(1, 10): 
            distance = [add_default] * 10
            distance[num] += add_one

            if 1 <= num + 1 <= 9: distance[num + 1] += 1
            else: distance[0] += 1

            if num == 9: distance[1] += 1
            current_count = [current_count[n] + distance[n] for n in range(10)]
            counts[(num + 1) * 10 ** depth] = current_count.copy()
    
    return counts

def get_number_count(input_number):
    numbers = list(map(int, str(input_number)))
    length = len(numbers)
    count_dp = generate_digit_counts(length)
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for idx in range(length):
        position, digit = length - idx, numbers[idx]

        influence = (10 ** (position - 1)) * digit
        
        count = [count[n] + count_dp[influence][n] for n in range(10)]
        
        if (position < length) and (digit != 0) and (position > 1):
            for additional_zeros in range(1, position): count[0] += int("9" * additional_zeros)

        for previous_digit in numbers[:idx]: count[previous_digit] += digit * (10 ** (position - 1))

    return count

def main():
    user_input = int(input())
    count = get_number_count(user_input)
    result_string = " ".join(map(str, count))
    return result_string

print(main())

