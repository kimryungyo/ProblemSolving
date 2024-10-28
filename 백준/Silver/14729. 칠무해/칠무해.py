def main():
    from sys import stdin
    input = stdin.readline
    int_f, float_f, range_f = int, float, range

    scores = [ 0 ] * 100001

    N = int_f(input())
    for _ in range_f(N):
        score = int_f(float_f(input()) * 1000)
        scores[score] += 1

    printed = 0
    for score in range_f(100001):
        if scores[score]:
            for i in range_f(scores[score]):
                print(f"{score / 1000:.3f}")
                printed += 1
                if printed == 7:
                    quit()

main()