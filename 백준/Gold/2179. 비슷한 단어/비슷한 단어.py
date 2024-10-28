from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())

prefixs = {}
max_len = 0
max_prefix = None

first = None
second = None


strings = []
for _ in range(n):
    string = input()
    strings.append(string)

results = [string[0], string[1]]

for string in strings:
    prefix = ""

    for char in string:
        prefix += char

        if prefix not in prefixs: prefixs[prefix] = []
        prefixs[prefix].append(string)
        
        if len(prefixs[prefix]) > 1:
            if len(prefix) > max_len:
                max_len = len(prefix)
                max_prefix = prefix

                results = []
                first = prefixs[max_prefix][0]
                second = prefixs[max_prefix][1]
                results.append( (first, second) )

            elif len(prefix) == max_len:
                first = prefixs[prefix][0]
                second = prefixs[prefix][1]
                results.append( (first, second) )

def sorting_key(answers):
    first, second = answers
    first_idx = strings.index(first)
    second_idx = strings.index(second)
    weight = first_idx * 1e6 + second_idx
    return weight

first, second = min(results, key=sorting_key)
print(first)
print(second)