class NonRecursionSegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 1

        while self.size < self.n:
            self.size <<= 1

        self.tree = [0] * (2 * self.size)

        for i in range(self.n):
            self.tree[self.size + i] = arr[i]

        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def sum_range(self, left, right):
        left += self.size
        right += self.size
        result = 0

        while left <= right:

            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            
            if right % 2 == 0:
                result += self.tree[right]
                right -= 1

            left //= 2
            right //= 2

        return result

    def update(self, index, value):
        
        index += self.size
        self.tree[index] += value

        while index > 1:
            index //= 2
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]

    def __len__(self): return self.n

    def __getitem__(self, index):
        return self.sum_range(0, index)

from bisect import bisect_left
from sys import stdin
input = stdin.readline

N = int(input())
segtree = NonRecursionSegmentTree( [0] * 2000002 )

for _ in range(N):
    Q, X = map(int, input().split())
    if Q == 1: segtree.update(X, 1)
    else:
        num = bisect_left(segtree, X)
        segtree.update(num, -1)
        print(num)