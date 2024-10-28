key = input()
cipher_text = input()
n = len(key)

num_rows = len(cipher_text) // n
columns = ['' for _ in range(n)]
sorted_key_indices = sorted(range(n), key=lambda i: key[i])

index = 0
for i in range(n):
    for j in range(num_rows):
        columns[sorted_key_indices[i]] += cipher_text[index]
        index += 1

plain_text = []
for row in range(num_rows):
    for col in range(n):
        plain_text.append(columns[col][row])

print("".join(plain_text))