def is_palindrome(start, end):
    length = end - start
    half_length = length // 2

    if length == 1: return True

    for i in range(half_length):
        if string[start + i] != string[end - i - 1]:
            return False

    return is_palindrome(start, start + half_length) and is_palindrome(end - half_length, end)

string = input()
print("AKARAKA" if is_palindrome(0, len(string)) else "IPSELENTI")