from sys import stdin
input = lambda: stdin.readline().rstrip()

fibo = [1,1]
while True:
    new_fibo = fibo[-2] + fibo[-1]
    fibo.append(new_fibo)
    if new_fibo >= 10 ** 100:
        break

while True:
    a,b = map(int , input().split())
    if a == b == 0: break

    s, e = 0, 0
    for i in range(0, len(fibo)):
        if fibo[i] >= a and s == 0: s = i
        if fibo[i] > b and e == 0: e = i

    print(e - s)