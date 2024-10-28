while True:
    word = input()
    if word == "#": break

    for char in word:
        if char in ['a', 'e', 'i', 'o', 'u']:
            while word[0] not in ['a', 'e', 'i', 'o', 'u']:
                word = word[1:] + word[0]
            break

    print(word + 'ay')