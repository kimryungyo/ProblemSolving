memoization = {}

def calculate_average(input_numbers: list, count: int = 0, indent = 0):
    global memoization
    if (input_numbers_str := str(input_numbers)) in memoization:
        return (memoization[input_numbers_str]["total"] + memoization[input_numbers_str]["possible_count"] * count) / memoization[input_numbers_str]["possible_count"]


    else:
        possible_index = set()

        possible_index = {
            (lower_idx, higher_idx) for lower_idx, lower in enumerate(input_numbers) for higher_idx, higher in enumerate(input_numbers)
            if (input_numbers.index(lower)) < (input_numbers.index(higher)) and lower > higher
        }

        if len(possible_index) == 0: return count / 1

        count += 1

        total = 0
        possible_count = len(possible_index)
        for change in possible_index:
            numbers = input_numbers.copy()
            numbers[change[0]], numbers[change[1]] = numbers[change[1]], numbers[change[0]]

            total += calculate_average(numbers, count, indent + 1)

        result = total / possible_count
        memoization[input_numbers_str] = {"possible_count": possible_count, "total": total - (count - 1) * possible_count}
        return result

def main():
    n = int(input())
    numbers = list(map(int, input().split()))

    average = calculate_average(numbers)
    return average

print(main())
