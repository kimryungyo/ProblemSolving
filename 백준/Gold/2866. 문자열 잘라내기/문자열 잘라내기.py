from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
table = [ list(input()) for _ in range(N) ]

words = table[N-1].copy()
words_set = set(words)

possible = [ True ] * (N)
if len(words_set) != M: possible[1] = False

leng = 1
for j in range(N - 2, -1, -1):
    leng += 1
    new_words = []
    new_words_set = set()
    for i in range(M):
        new_word = words[i] + table[j][i]
        new_words.append(new_word)
        if new_word in new_words_set:
            possible[leng] = False
        new_words_set.add(new_word)

    words = new_words
    new_words_set = set()

count = 0
while len(possible) > 1:
    value = possible.pop()
    if value is True: count += 1
    else: break
    
print(count)