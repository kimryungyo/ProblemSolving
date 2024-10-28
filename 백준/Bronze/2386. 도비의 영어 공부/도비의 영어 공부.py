while True:
    array = input().split(maxsplit=1)
    if len(array) == 1: break

    char, string = array
    print(char, string.lower().count(char))