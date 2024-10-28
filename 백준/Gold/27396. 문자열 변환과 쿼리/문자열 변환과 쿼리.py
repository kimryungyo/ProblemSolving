from sys import stdin
input = stdin.readline

refers = [ { chr(ascii) } for ascii in range(150) ]
string, N = input().split()

for _ in range(int(N)):
    question, *query = input().split()

    if query:
        a, b = map(ord, query)

        small_refer, big_refer = sorted([refers[a], refers[b]], key=len)
        big_refer |= small_refer
        refers[a] = set()
        refers[b] = big_refer

    else:
        match = {}
        for ascii in range(65, 123):
            result = chr(ascii)
            for char in refers[ascii]:
                match[char] = result
        
        array = []
        for char in string: array.append(match[char])
        print("".join(array))