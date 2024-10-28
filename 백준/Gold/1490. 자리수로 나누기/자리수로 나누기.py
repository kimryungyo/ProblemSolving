def lcm(a, b): return a * b // gcd(a, b)
def gcd(a, b): return b if a % b == 0 else gcd(b, a % b)

number_input = input()
digits_list = list(map(int, filter(lambda x: x != '0', number_input)))

lcm_value = digits_list[0]
for i in range(1, len(digits_list)): lcm_value = lcm(lcm_value, digits_list[i])

num = int(number_input)
size_value = 1

while True:
    temp_value = num * size_value
    for i in range(size_value):
        if temp_value % lcm_value == 0: print(temp_value); break
        temp_value += 1
    else: size_value *= 10; continue
    break

