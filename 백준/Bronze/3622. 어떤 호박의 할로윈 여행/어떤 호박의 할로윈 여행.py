a1, a2, b1, b2, p = map(int, input().split())
print('Yes' if (a1 + b1 <= p or a2 >= b1 or b2 >= a1) and a1 <= p and b1 <= p else 'No')