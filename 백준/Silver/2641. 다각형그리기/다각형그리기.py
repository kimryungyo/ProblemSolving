def reverse_shape(n: list):
    n.reverse()
    a = list()
    for draw in n:
        if draw == 1: a.append(3)
        elif draw == 3: a.append(1)
        elif draw == 2: a.append(4)
        else: a.append(2)
    return a

def rotate_shape(n: list):
    length = len(n)
    for i in range(length):
        yield n[i:] + n[:i]

def main():
    m = int(input())
    r = list(map(int, input().split()))

    b = int(input())

    d = []
    for i in range(b):
        e = input()
        c = list(map(int, e.split()))

        cs = [c, reverse_shape(c.copy())]

        u = False
        for c in cs:
            for q in rotate_shape(c):
                if r == q:
                    u = True
                    break
            if u == True: break

        if u == True: d.append(e)
        
    print(len(d))
    for o in d: print(o)

main()

