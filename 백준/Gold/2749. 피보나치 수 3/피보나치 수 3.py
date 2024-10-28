fibonacci = [0, 1]
add1, add2 = 0, 1
for i in range(1500000 - 2):
    temp = (add1 + add2) % 1000000
    add1, add2 = add2, temp
    fibonacci.append(temp)

n = int(input())
print(fibonacci[n % 1500000])