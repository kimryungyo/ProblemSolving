from sys import stdin
input = lambda: stdin.readline().rstrip()

n, q = map(int, input().split())
nums = list(map(int, input().split()))

class SegmentTree():
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (self.n * 2)
        
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
    
    def set(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[pos * 2] + self.tree[pos * 2 + 1]
    
    def sum(self, l, r):
        result = 0
        l += self.n
        r += self.n
        while l < r:
            if l % 2 == 1:
                result += self.tree[l]
                l += 1
            if r % 2 == 1:
                r -= 1
                result += self.tree[r]
            l //= 2
            r //= 2
        return result

tree = SegmentTree(nums)
for _ in range(q):
    x, y, a, b = map(int, input().split())
    if x > y: x, y = y, x
    x, y, a = x - 1, y - 1, a - 1
    
    print(tree.sum(x, y + 1))
    tree.set(a, b)