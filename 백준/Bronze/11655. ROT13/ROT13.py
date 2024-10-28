for char in input():

    lower = False
    if char != char.upper():
        lower = True
        char = char.upper()
    
    code = ord(char)
    if (code >= 65 and code <= 90):
        code -= 65
        code += 13
        code %= 26
        code += 65
        char = chr(code)
        if lower: char = char.lower()

    print(char, end = "")