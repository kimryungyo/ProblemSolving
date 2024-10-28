n = int(input())
v, r = [0] * 1000004, [0] * 1000004
p = list(map(int, input().split()))

def check(card_n):
    if card_n == 1: return
    for i in range(1, int(card_n**0.5) + 1):
        if card_n % i == 0:
            if v[i] == 1:
                r[i] += 1
                r[card_n] -= 1
            if v[card_n // i] == 1 and i*i != card_n:
                r[card_n // i] += 1
                r[card_n] -= 1

for card in p: v[card] = 1
for card in p: check(card)
for card in p: print(r[card], end=' ')