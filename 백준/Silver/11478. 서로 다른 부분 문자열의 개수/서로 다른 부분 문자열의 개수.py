S = input()
substrings = set()
for i in range(len(S)):
    substring = ""
    for j in range(i, len(S)):
        substring += S[j]
        substrings.add(substring)
print(len(substrings))