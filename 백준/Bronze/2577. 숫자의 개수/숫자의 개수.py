A = int(input())
B = int(input())
C = int(input())

result = A * B * C
count_list = [0] * 10

for num in str(result): count_list[int(num)] += 1
for count in count_list: print(count)