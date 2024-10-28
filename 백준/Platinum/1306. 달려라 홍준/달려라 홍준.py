from sys import stdin
input = lambda: stdin.readline().rstrip()

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
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, left, right, node, node_left, node_right):
        if right < node_left or left > node_right:
            return float('-inf')
        if left <= node_left and right >= node_right:
            return self.tree[node]
        mid = (node_left + node_right) // 2
        return max(self.query(left, right, 2 * node, node_left, mid), self.query(left, right, 2 * node + 1, mid + 1, node_right))

    def max_range(self, left, right):
        return self.query(left, right, 1, 0, self.size - 1)

    def update(self, index, value):
        index += self.size
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = max(self.tree[2 * index], self.tree[2 * index + 1])

N, M = map(int, input().split())
BOARDS = list(map(int, input().split()))

seg_tree = SegmentTree(BOARDS)
for player in range(M-1, N-M+1):
    light = seg_tree.max_range(player - (M-1), player + (M-1))
    print(light, end = " ")