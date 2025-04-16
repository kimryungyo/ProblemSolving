graph = {
    '1': {'4','5'},
    '2': set(),
    '3': {'4','5'},
    '4': {'2','3'},
    '5': {'8'},
    '6': {'2','3'},
    '7': {'8'},
    '8': {'6','7'},
}

case_no = 1
while True:
    s = input().strip()
    if s == '0':
        break
    valid = s[0] == '1' and s[-1] == '2'
    if valid:
        for a, b in zip(s, s[1:]):
            if b not in graph[a]:
                valid = False
                break
    print(f"{case_no}. {'VALID' if valid else 'NOT'}")
    case_no += 1