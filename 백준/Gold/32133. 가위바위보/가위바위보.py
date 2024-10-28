from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M, K = map(int, input().split())

friend_cards = [ list(input()) for _ in range(N) ]

min_round = M + 1
min_cards = None

def is_win(me, other):
    if me == "R" and other == "S": return True
    elif me == "S" and other == "P": return True
    elif me == "P" and other == "R": return True
    else: return False

def dfs(friends, round, history = ""):
    global min_round, min_cards
    for card in ["R", "S", "P"]:
        next_players = [ friend for friend in friends if is_win(friend_cards[friend][round - 1], card) ]
        if next_players:
            if len(next_players) > K:
                if round < M: dfs(next_players, round + 1, history + card)
            elif round < min_round:
                min_round = round
                min_cards = history + card

dfs(range(N), 1)
if min_cards: 
    print(min_round)
    print(min_cards)
else:
    print(-1)