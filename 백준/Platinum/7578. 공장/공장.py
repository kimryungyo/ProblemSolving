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

N = int(input())
upper = list(map(int, input().split()))
lower = list(map(int, input().split()))
indexs = { v: i for i, v in enumerate(lower) }

segtree_lower = SegmentTree([0] * N)

cross = 0
for num in upper:
    idx = indexs[num]
    segtree_lower.update(idx, 1)
    right_sum = segtree_lower.sum_range(idx + 1, N - 1)
    cross += right_sum

print(cross)