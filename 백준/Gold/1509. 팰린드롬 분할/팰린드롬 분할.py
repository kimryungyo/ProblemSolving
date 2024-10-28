string = input()
string_len = len(string) 

dp = [2500 for _ in range(string_len + 1)]
dp[-1] = 0
is_p = [[0 for j in range(string_len)] for i in range(string_len)]


for i in range(string_len): is_p[i][i] = 1

for i in range(1, string_len):
    if string[i - 1] == string[i]:
        is_p[i - 1][i] = 1

for l in range(3, string_len + 1):
    for start in range(string_len - l + 1):
        end = start + l - 1
        if string[start] == string[end] and is_p[start + 1][end - 1]:
            is_p[start][end] = 1

def min_palindrome_partitions():
    dp = [float('inf')] * string_len
    
    for i in range(string_len):
        if is_p[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if is_p[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)
    
    return dp[-1] + 1

print(min_palindrome_partitions())