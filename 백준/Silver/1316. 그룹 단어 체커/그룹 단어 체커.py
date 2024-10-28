from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
count = 0

for _ in range(n):
    word = input()
    group_word = True

    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                group_word = False
                break

    if group_word:
        count += 1

print(count)