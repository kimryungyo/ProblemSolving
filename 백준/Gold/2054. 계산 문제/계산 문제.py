from collections import deque

number = input()
length = len(number)

def split_number(n):
    result = []
    
    def backtrack(curr_list, remaining):
        if remaining == 0:
            result.append(curr_list[:])
            return
        for i in range(1, remaining + 1):
            curr_list.append(i)
            backtrack(curr_list, remaining - i)
            curr_list.pop()
    
    backtrack([], n)
    
    return result

def expression_cases(nums):
    new_exps = []
    exp_len = len(nums) - 1
    queue = deque([ ["*"], ["-"], ["+"] ])

    while queue:
        exp = queue.popleft()
        if len(exp) == exp_len:
            new_exps.append(exp)

        else:
            for next in [ ["*"], ["-"], ["+"] ]:
                new_exp = exp + next
                queue.append(new_exp)

    return new_exps


cases = []
split_cases = split_number(length)
for splits in split_cases:
    if len(splits) == 1: continue

    nums = []
    s = 0
    for l in splits:
        num = number[s:s+l]
        nums.append(num)
        s += l

    passes = False
    for num in nums:
        if num[0] == "0":
            if num != "0":
                passes = True
    if passes: continue

    exps = expression_cases(nums)
    for exp in exps:
        expression = nums[0]

        for i in range(len(exp)):
            expression += exp[i]
            expression += nums[i+1]

        if eval(expression) == 2000:
            cases.append(expression)

if cases:
    print(*sorted(cases), sep="\n")
