N, *array = map(int, open(0))

left_count = 1
max = array[0]
for height in array:
    if height > max:
        left_count += 1
        max = height

right_count = 1
max = array[-1]
for height in reversed(array):
    if height > max:
        right_count += 1
        max = height

print(left_count)
print(right_count)