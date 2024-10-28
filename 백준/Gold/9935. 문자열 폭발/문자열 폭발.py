string = input()
bomb = list(input())
leng = len(bomb)

result = []
for i in range(len(string)):
    result.append(string[i])

    while result[max(0, len(result) - leng):] == bomb:
        del result[-leng:]

print("".join(result if result else "FRULA"))