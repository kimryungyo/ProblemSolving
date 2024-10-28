k = int(input())
total_sum = (2 ** k - 1) * 2 ** (k-1)
print(bin(total_sum)[2:])