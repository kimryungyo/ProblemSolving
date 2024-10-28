def check_possibility(a: list):
    b = 1422 * 2
    for c in a.copy(): a.append(b - c)
    a.sort()
    for i in range(len(a) - 1):
        if a[i + 1] - a[i] > 200: return "IMPOSSIBLE"
    return "POSSIBLE"
def main():
    while True:
        d = int(input())
        if d == 0: break
        a = []
        for i in range(d): a.append(int(input()))
        print(check_possibility(a))
main()
