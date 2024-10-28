from sys import stdin
input = stdin.readline

MOD = 10 ** 9 + 7

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)

        self.size = 1
        while self.size < self.n:
            self.size *= 2

        self.tree = [ [0, 0] for _ in range(2 * self.size) ]

    def query(self, left, right, node, node_left, node_right):
        if right < node_left or left > node_right:
            return (0, 0)
        if left <= node_left and right >= node_right:
            return self.tree[node]
        
        mid = (node_left + node_right) // 2
        return self.sum_nodes(self.query(left, right, 2 * node, node_left, mid), self.query(left, right, 2 * node + 1, mid + 1, node_right))

    def sum_range(self, left, right):
        return self.query(left, right, 1, 0, self.size - 1)

    def update(self, index, value):
        index += self.size
        self.tree[index][0] += 1
        self.tree[index][1] += value

        while index > 1:
            index //= 2
            self.tree[index] = self.sum_nodes(self.tree[2 * index], self.tree[2 * index + 1])

    def sum_nodes(self, *nodes):
        count = sum = 0
        for node in nodes:
            node_count, node_sum = node
            count += node_count
            sum += node_sum
        return (count, sum)

    def __getitem__(self, index):
        return self.tree[self.size + index]
    
N, *trees = map(int, open(0))
total_price = 0

tree_segtree = SegmentTree([ None ] * 200002)

for tree in trees: 
    left_count, left_sum = tree_segtree.sum_range(0, tree)
    right_count, right_sum = tree_segtree.sum_range(tree, 200001)

    left_price = (tree * left_count) - left_sum
    right_price = right_sum - (tree * right_count)
    tree_price = left_price + right_price

    if total_price == 0:
        total_price = tree_price
        
    elif tree_price > 0: 
        total_price *= tree_price
        total_price %= MOD

    tree_segtree.update(tree, tree)

print(total_price)