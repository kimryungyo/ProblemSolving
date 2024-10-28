from sys import stdin
input = lambda: stdin.readline().rstrip()

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)

        self.size = 1
        while self.size < self.n:
            self.size *= 2

        self.tree = [(1000000000, 1)] * (2 * self.size)

        for i in range(self.n):
            self.tree[self.size + i] = (arr[i], arr[i])

        for i in range(self.size - 1, 0, -1):
            min_left, max_left = self.tree[2 * i]
            min_right, max_right = self.tree[2 * i + 1]
            self.tree[i] = ( min(min_left, min_right), max(max_left, max_right) )

    def query(self, left, right, node, node_left, node_right):
        if right < node_left or left > node_right:
            return (1000000000, 1)
        if left <= node_left and right >= node_right:
            return self.tree[node]
        mid = (node_left + node_right) // 2
        
        min_left, max_left = self.query(left, right, 2 * node, node_left, mid)
        min_right, max_right = self.query(left, right, 2 * node + 1, mid + 1, node_right)
        
        return ( min(min_left, min_right), max(max_left, max_right) )

    def sum_range(self, left, right):
        return self.query(left, right, 1, 0, self.size - 1)

    def update(self, index, value):
        index += self.size
        self.tree[index] = value
        while index > 1:
            index //= 2
            min_left, max_left = self.tree[2 * index]
            min_right, max_right = self.tree[2 * index + 1]
            self.tree[index] = ( min(min_left, min_right), max(max_left, max_right) )

    def __getitem__(self, index):
        return self.tree[self.size + index]
    
N, M = map(int, input().split())
nums = [ int(input()) for _ in range(N) ]
segtree = SegmentTree(nums)

for _ in range(M):
    A, B = map(int, input().split())
    minimum, maximum = segtree.sum_range(A - 1, B - 1)
    print(minimum, maximum)