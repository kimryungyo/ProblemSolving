while True:
    string = input()
    if string == "0": break

    is_palindrome = True
    for i in range(len(string)):
        if string[i] != string[-i-1]:
            is_palindrome = False
            break

    print("yes" if is_palindrome else "no")