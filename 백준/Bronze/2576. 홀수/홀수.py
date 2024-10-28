nums = [ int(input()) for _ in range(7) ]
odd_numbers = [ num for num in nums if num % 2 == 1 ]
if not odd_numbers: print(-1); quit()
print(sum(odd_numbers))
print(min(odd_numbers))