def sum(x, y):
    carry = 0
    result = ""

    x = x[::-1]
    y = y[::-1]

    while len(x) < len(y): x += '0'
    while len(x) > len(y): y += '0'

    for i in range(len(x)):
        num = (int(x[i]) + int(y[i]) + carry) % 10
        result += str(num)
        carry = (int(x[i]) + int(y[i]) + carry) // 10

    if carry != 0: result += str(carry)
    result = result[::-1]
    return result

n = int(input())
a = '0'
b = '1'
result = ""

if n == 0: result = "0"
if n == 1: result = "1"

for i in range(2, n+1):
    result = sum(a, b)
    a = b
    b = result

print(result)
