T = int(input())
for case in range(1, T + 1):
    A, B = map(int, input().split())
    C = A + B
    print(f"Case #{case}: {A} + {B} = {C}")