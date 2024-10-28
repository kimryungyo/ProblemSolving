def cp(a):
    f = [1, 1]
    for i in range(1, int(1e10)):
        r = (f[0] + f[1]) % a
        f = [f[1], r]
        if f == [1, 1]: break
    return i
def main():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        print(n, cp(m))
main()
