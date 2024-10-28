BASE_CHR = "".join( [ chr(asc) for asc in range(33, 126) ] )

class BaseN():
    def __init__(self, n, num):
        self.n = n

        num_type = type(num)
        if num_type == str: self.base = num
        elif num_type == int: self.decimal = num

    @property
    def base(self): return self._base

    @base.setter
    def base(self, base):
        self._base = base

        negative = True if base[0] == "~" else False
        base_abs = base[1:] if base[0] == "~" else base

        self._decimal, impact = 0, 1
        for char in base_abs[::-1]:
            self._decimal += BASE_CHR.index(char) * impact
            impact *= self.n

        if negative == True: self._decimal *= -1

    @property
    def decimal(self): return self._decimal

    @decimal.setter
    def decimal(self, decimal):
        self._decimal = decimal
        if decimal == 0: 
            self._base = BASE_CHR[0]
            return
        
        num = decimal if decimal > 0 or self.n < 0 else decimal * -1

        self._base = ""
        for power in range(int(1e10)):
            modular = num // (self.n ** power) % abs(self.n)
            self._base = BASE_CHR[modular] + self._base
            num -= modular * (self.n ** power)
            if num == 0: break

        if decimal < 0 and self.n > 0: self._base = "~" + self._base

def main():
    n = int(input())
    base1 = BaseN(n, input())
    base2 = BaseN(n, input())
    base3 = BaseN(n, base1.decimal * base2.decimal)
    print(base3.base)

main()