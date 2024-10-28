characters, password = [], []
length = num = vowel = value = 0

def generate_password(start, cnt):
    global vowel, value
    if cnt == length:
        vowel = value = 0
        for i in range(len(password)):
            if password[i] in ['a', 'e', 'i', 'o', 'u']: vowel += 1
            else: value += 1
        if vowel >= 1 and value >= 2: print(''.join(password))
        return

    for i in range(start, len(characters)):
        password.append(characters[i])
        generate_password(i + 1, cnt + 1)
        password.pop()

if __name__ == "__main__":
    length, num = map(int, input().split())
    characters = list(input().split())
    characters.sort()
    generate_password(0, 0)
