binary = input()
before = -1
count = [0, 0]
for bit in binary:
    if bit != before:
        if bit == "1": count[1] += 1
        else: count[0] += 1
        before = bit
print(min(count))