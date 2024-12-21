import math

N = int(input())
A = list(map(int, input().split()))
sum_num = 0
sum_den = 1

for a in A:
    current_num = 1
    current_den = a
    new_num = sum_num * current_den + sum_den * current_num
    new_den = sum_den * current_den
    gcd = math.gcd(new_num, new_den)
    sum_num = new_num // gcd
    sum_den = new_den // gcd
    
harmonic_num = sum_den
harmonic_den = sum_num
final_gcd = math.gcd(harmonic_num, harmonic_den)
harmonic_num //= final_gcd
harmonic_den //= final_gcd
print(f"{harmonic_num}/{harmonic_den}")