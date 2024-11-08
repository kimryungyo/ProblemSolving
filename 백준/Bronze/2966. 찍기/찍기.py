N = int(input())
answers = input()

adrian = 'ABC' * (N // 3) + 'ABC'[:N % 3]
bruno = 'BABC' * (N // 4) + 'BABC'[:N % 4]
goran = 'CCAABB' * (N // 6) + 'CCAABB'[:N % 6]

adrian_score = sum(1 for i in range(N) if answers[i] == adrian[i])
bruno_score = sum(1 for i in range(N) if answers[i] == bruno[i])
goran_score = sum(1 for i in range(N) if answers[i] == goran[i])

max_score = max(adrian_score, bruno_score, goran_score)

winners = []
if adrian_score == max_score:
    winners.append('Adrian')
if bruno_score == max_score:
    winners.append('Bruno')
if goran_score == max_score:
    winners.append('Goran')

print(max_score)
for winner in winners:
    print(winner)