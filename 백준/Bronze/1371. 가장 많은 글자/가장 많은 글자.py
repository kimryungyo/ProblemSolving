lines = open(0).read().split()

freq = {}
for line in lines:
    for char in line:
        if char.isalpha():
            if char in freq: freq[char] += 1
            else: freq[char] = 1

max_freq = max(freq.values())
most_frequent_chars = [char for char, count in freq.items() if count == max_freq]

most_frequent_chars.sort()

print(''.join(most_frequent_chars))