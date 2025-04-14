N = int(input())
S = input()

ans = 0
for i in range(N-2):
    if S[i] == 'A':

        for j in range(i+2, N):
            if S[j] == 'A':

                mid = S[i+1:j]
                if mid.count('N') == 1 and mid.count('A') == 0:
                    ans += 1
print(ans)