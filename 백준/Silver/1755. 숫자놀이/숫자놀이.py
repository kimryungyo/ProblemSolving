num_engs = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

def number_to_english(num):
    num_str = str(num)
    english = ""
    for number in num_str:
        english += num_engs[number]
    return english

M, N = map(int, input().split())
nums = [ i for i in range(M, N + 1) ]
nums.sort(key=number_to_english)

for i in range(len(nums)):
    end_str = " " if (i + 1) % 10 else "\n"
    print(nums[i], end = end_str)