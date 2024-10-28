N = int(input())

players = []

for _ in range(N):
    player = input()
    players.append(player)

count_dict = {}

for player in players:
    first_letter = player[0]
    if first_letter in count_dict:
        count_dict[first_letter] += 1
    else:
        count_dict[first_letter] = 1

selected_players = []

for key, value in count_dict.items():
    if value >= 5:
        selected_players.append(key)

if not selected_players:
    print("PREDAJA")
else:
    selected_players.sort()
    print("".join(selected_players))