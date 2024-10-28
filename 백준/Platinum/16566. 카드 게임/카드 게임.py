from bisect import bisect_left
N, M, K = map(int, input().split())

cards = sorted(map(int, input().split()))
cards_valid = [ True ] * (M + 1)

opponent_order = list(map(int, input().split()))

for opponent in opponent_order:
    my_card_idx = bisect_left(cards, opponent + 1)
    while cards_valid[my_card_idx] is False:
        my_card_idx += 1

    print(cards[my_card_idx])
    cards_valid[my_card_idx] = False