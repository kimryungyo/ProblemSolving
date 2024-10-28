from sys import stdin
input = lambda: stdin.readline().rstrip()

class Node:
    def __init__(self):
        self.child = {}

    def insert(self, value, idx):
        if idx == len(value): return
        if value[idx] in self.child:
            self.child[value[idx]].insert(value, idx + 1)
        else:
            n = Node()
            self.child[value[idx]] = n
            n.insert(value, idx + 1)

    def print(self, idx):
        for key in sorted(self.child.keys()):
            value = self.child[key]
            for i in range(idx): print("--", end="")
            print(key)
            value.print(idx + 1)


root = Node()

n = int(input())
for _ in range(n):
    K, *values = input().split()
    K = int(K)
    root.insert(values, 0)

root.print(0)
