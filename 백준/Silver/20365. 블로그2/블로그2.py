n = int(input())
s = input()

bcount = 0
rcount = 0

prev = ''
for c in s:
    if c != prev:
        if c == 'B':
            bcount += 1
        else:
            rcount += 1
        prev = c

print(1 + min(bcount, rcount))