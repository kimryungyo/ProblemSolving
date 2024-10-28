def solve():
    p = int(input())
    n = int(input())
    v = [0] * 100

    for _ in range(n):
        a, b = input().split()
        a = int(a)

        if b == 'L':
            for i in range(a-2, -1, -1):
                v[i] = (v[i] + 1) % 3

        else:
            for i in range(a, 100):
                v[i] = (v[i] + 1) % 3

    ans = 0.01 * p
    for i in range(3):
        print(f"{ans * v.count(i):.2f}")
 
solve()