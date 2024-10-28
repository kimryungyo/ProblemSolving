str_1 = input()
str_2 = input()

table = [ [0] * (len(str_1) + 1) for _ in range(len(str_2) + 1) ]

max_len = 0
max_pos = None

for i in range(1, len(str_1) + 1):
    for j in range(1, len(str_2) + 1):
        if str_1[i - 1] == str_2[j - 1]:
            table[j][i] = table[j-1][i-1] + 1
        else:
            table[j][i] = max(table[j-1][i], table[j][i-1])
        if table[j][i] > max_len:
            max_len = table[j][i]
            max_pos = (j, i)

string = ""
j, i = max_pos

while table[j][i] > 0:
    if table[j-1][i] == table[j][i]:
        j -= 1
    elif table[j][i-1] == table[j][i]:
        i -= 1
    else:
        j -= 1
        i -= 1
        string = str_1[i] + string

print(string)