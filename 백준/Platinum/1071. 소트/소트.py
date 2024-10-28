def sort_numbers(input_numbers: list, sorted_numbers: list):

    if input_numbers == []: return sorted_numbers

    previous_num = sorted_numbers[-1]
    valid_numbers = sorted([num for num in set(input_numbers) - {previous_num + 1}])

    for next_number in valid_numbers:
        numbers, sorted_nums = input_numbers.copy(), sorted_numbers.copy()
        numbers.remove(next_number)
        sorted_nums.append(next_number)

        result = sort_numbers(numbers, sorted_nums)
        if result != False: return result

    return False
    
def main():
    n = int(input())
    numbers = list(map(int, input().split()))

    for start_num in sorted(list(set(numbers))):
        input_nums = numbers.copy()
        input_nums.remove(start_num)

        result = sort_numbers(input_nums, [start_num])
        if result != False: return " ".join(map(str, result))

print(main())

