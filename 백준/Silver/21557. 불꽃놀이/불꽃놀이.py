def main(fpc: int = None, fl: str = None) -> int:
    if fpc == None: fpc = int(input())
    if fl == None: fl = input()
    fpe = [int(fl.split(" ", 1)[0]), int(fl.rsplit(" ", 1)[1])]
    del fl
    afc = fpc - 2
    fpe.sort()
    h, l = fpe[1], fpe[0]
    hd = h - l
    if hd >= afc: return h - afc
    else:
        h -= hd
        afc -= hd
        fpc -= hd
        f = h
        ef = afc // 2
        f -= ef
        afc -= ef * 2
        if afc == 1: return f - 1
        else: return f

print(main())