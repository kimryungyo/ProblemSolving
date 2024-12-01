from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
players = list(map(int, input().split()))

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)

        self.size = 1
        while self.size < self.n:
            self.size *= 2

        self.tree = [0] * (2 * self.size)

        for i in range(self.n):
            self.tree[self.size + i] = arr[i]

        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def query(self, left, right, node, node_left, node_right):
        if right < node_left or left > node_right:
            return 0
        if left <= node_left and right >= node_right:
            return self.tree[node]
        mid = (node_left + node_right) // 2
        return self.query(left, right, 2 * node, node_left, mid) + self.query(left, right, 2 * node + 1, mid + 1, node_right)

    def sum_range(self, left, right):
        return self.query(left, right, 1, 0, self.size - 1)

    def update(self, index, value):
        index += self.size
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]

    def __getitem__(self, index):
        return self.tree[self.size + index]
    
def find_matchs(players, compress = False):
    if compress:
        order = sorted(players)
        idxs = { v: i for i, v in enumerate(order) }
        compressed = [ idxs[num] + 1 for num in players ]
        players = compressed

    players = deque(players)

    leng = len(players)

    heights = [ 0 ] * (leng + 1)
    for height in players:
        if height % 2 == 0 or compress:
            heights[height] = 1
    tree = SegmentTree(heights)

    matchs = 0
    while players:
        height = players.popleft()
        if height % 2 == 0 or compress:
            tree.update(height, 0)
            matchs += tree.sum_range(0, height)

    return matchs
    
matchs = 0
matchs += find_matchs(players)

players.append(-1)
even_heights = [] 
for height in players:
    if height % 2 == 0: even_heights.append(height)
    else:
        if len(even_heights) > 1:
            matchs -= find_matchs(even_heights, compress = True)
        even_heights = []

print(matchs)