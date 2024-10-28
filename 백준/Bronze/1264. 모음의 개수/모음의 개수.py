while (string := input()) != "#":
    total = 0
    for char in "aeiou":
        total += string.lower().count(char)
    print(total)