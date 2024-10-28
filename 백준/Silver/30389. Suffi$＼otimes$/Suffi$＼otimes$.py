def main():
    from sys import stdin
    input = lambda: stdin.readline().rstrip()
    l = len

    counts = {}

    N = int(input())
    for _ in range(N):
        string = input()

        for i in range(1, l(string) + 1):
            sub_string = string[-i:]
            if sub_string not in counts: 
                counts[sub_string] = True
            else:
                counts[sub_string] = not counts[sub_string]

    
    res = list(counts.values()).count(True)
    print(res)

main()