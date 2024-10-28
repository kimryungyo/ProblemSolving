from fractions import Fraction

test = 0
while True:
    test += 1
    n = int(input())
    if n == 0: break
    fracs = []
    for _ in range(n):
        string = input()

        if "," in string:
            integer, frac = string.split(",")
            nume, deno = map(int, frac.split("/"))
            nume += int(integer) * deno

        elif "/" in string:
            nume, deno = map(int, string.split("/"))

        else:
            nume, deno = int(string), 1

        fracs.append(Fraction(nume, deno))

    sum_ = sum(fracs)
    nume, deno = sum_.numerator, sum_.denominator

    print(f"Test {test}:", end = " ")
    if deno == 1: print(nume)
    elif nume < deno: print(f"{nume}/{deno}")
    else:
        print(nume // deno, end=",")
        print(nume % deno, end="/")
        print(deno)