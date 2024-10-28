from sys import stdin
input = stdin.readline

while True:
    try: X = int(input()) * 10000000
    except: break

    N = int(input())
    blocks = {}
    for _ in range(N):
        block = int(input())
        if block not in blocks: blocks[block] = 0
        blocks[block] += 1
    block_1 = block_2 = None
    max_distance = -1
    for block in blocks.keys():
        other = X - block
        if other in blocks:

            if other == block and blocks[block] == 1:
                continue
            
            distance = abs(block - other)
            if distance > max_distance:
                block_1, block_2 = sorted([block, other])
                max_distance = distance

    if block_1 and block_2:
        print("yes", block_1, block_2)
    else:
        print("danger")