from sys import stdin
from collections import deque

input = stdin.readline
card_count, max_moves = map(int, input().split())

decks = [deque(), deque()]
temp_stacks = [deque(), deque()]

for _ in range(card_count):
    card_player1, card_player2 = map(int, input().split())
    decks[0].appendleft(card_player1)
    decks[1].appendleft(card_player2)

current = 0

for _ in range(max_moves):
    if not decks[current]:
        break
    temp_stacks[current].appendleft(decks[current].popleft())

    if not decks[0] or not decks[1]:
        break

    result = -1

    for i in range(2):
        if temp_stacks[i] and temp_stacks[i][0] == 5:
            result = 0

    if temp_stacks[0] and temp_stacks[1] and (temp_stacks[0][0] + temp_stacks[1][0] == 5):
        result = 1

    if result != -1:
        for i in [1 - result, result]:
            while temp_stacks[i]:
                decks[result].append(temp_stacks[i].pop())

    current = 1 - current

len_player1 = len(decks[0])
len_player2 = len(decks[1])

if len_player1 > len_player2:
    print('do')
elif len_player2 > len_player1:
    print('su')
else:
    print('dosu')