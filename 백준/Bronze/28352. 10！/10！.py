from math import factorial
n = int(input())
result = factorial(n)
weeks = result // (7 * 24 * 60 * 60)
print(weeks)