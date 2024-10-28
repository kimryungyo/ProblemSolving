number = list(map(int, input()))
distance = 0

power = 0
for num in reversed(number):
    if num > 4: num -= 1
    distance += (9 ** power) * num 
    power += 1

print(distance)