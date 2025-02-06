def convert_to_index(char):
    if char == "A": return 0
    if char == "E": return 1
    if char == "I": return 2
    if char == "O": return 3
    if char == "U": return 4

def input_datas():
    N = int(input())
    WORDS = []
    for idx in range(N):
        word = input()
        w_start = convert_to_index(word[0])
        w_end = convert_to_index(word[-1])
        info = (w_start, w_end, len(word), idx)
        WORDS.append(info)
    return N, WORDS

def main():
    N, WORDS = input_datas()
    created = [ [ False ] * 5 for _ in range(65536) ]

    queue = []
    initial = int('1' * N, 2)
    for start, end, leng, idx in WORDS:
        used = initial & ~(1 << idx)
        queue.append( (used, leng, end) )
        created[used][end] = True
    del initial

    max_len = 0
    while queue:
        used, leng, end = queue.pop()
        if leng > max_len:
            max_len = leng

        for i in range(N):
            if used & (1 << i):
                w_start, w_end, w_len, w_idx = WORDS[i]

                new_used = used & ~(1 << w_idx)
                new_len = leng + w_len

                if w_start == end and not created[new_used][w_end]:
                    created[new_used][w_end] = True
                    queue.append( (new_used, new_len, w_end) )

    return max_len

print(main())