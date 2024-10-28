def rev(n):
    return int(str(n)[::-1])

X, Y = map(int, input().split())

reversed_X = rev(X)
reversed_Y = rev(Y)
sum_reversed = reversed_X + reversed_Y
result = rev(sum_reversed)

print(result)