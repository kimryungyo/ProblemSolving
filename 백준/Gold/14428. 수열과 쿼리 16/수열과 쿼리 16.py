from sys import stdin
input = lambda: stdin.readline().rstrip()

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 1

        while self.size < self.n:
            self.size *= 2

        self.tree = [(0, 0)] * (2 * self.size)

        for i in range(self.n):
            self.tree[self.size + i] = (arr[i], i)

        for i in range(self.size - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, left, right, node, node_left, node_right):
        if right < node_left or left > node_right:
            return (float('inf'), -1)
        
        if left <= node_left and right >= node_right:
            return self.tree[node]
        
        mid = (node_left + node_right) // 2

        return min(self.query(left, right, 2*node, node_left, mid),
                   self.query(left, right, 2*node+1, mid+1, node_right))

    def min_range(self, left, right):
        return self.query(left, right, 1, 0, self.size - 1)

    def update(self, index, value):
        index += self.size
        self.tree[index] = (value, index - self.size)
        while index > 1:
            index //= 2
            self.tree[index] = min(self.tree[2 * index], self.tree[2 * index + 1])

N = int(input())
nums = list(map(int, input().split()))
segtree = SegmentTree(nums)

M = int(input())
for _ in range(M):
    query = list(map(int, input().split()))
    if query[0] == 1: segtree.update(query[1] - 1, query[2])
    else:
        _, index = segtree.min_range(query[1] - 1, query[2] - 1)
        print(index + 1)