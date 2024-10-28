A, B = map(int, input().split())
ERA = A - A * (B / 100)
print(1 if ERA < 100 else 0)