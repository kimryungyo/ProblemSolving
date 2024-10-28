def most_frequent_char(word):
    word = word.upper()
    freq = {}
    
    for char in word:
        if char in freq:
            freq[char] += 1

        else:
            freq[char] = 1

    max_freq = max(freq.values())
    most_freq_chars = [char for char, count in freq.items() if count == max_freq]

    if len(most_freq_chars) > 1:
        return '?'

    else:
        return most_freq_chars[0]

word = input().strip()
print(most_frequent_char(word))