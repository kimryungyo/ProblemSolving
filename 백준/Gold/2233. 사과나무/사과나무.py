N = int(input())
binary = list(input())
X, Y = map(int, input().split())

depths = [ None ] * N
parents = [ None ] * N

stack = []
mapping = []

depth = 0
new_node = 0
for bit in binary:
    if bit == "0":

        depths[new_node] = depth
        parents[new_node] = stack[-1] if stack else None

        stack.append(new_node)
        mapping.append(new_node)

        new_node += 1
        depth += 1
    else:
        node = stack.pop()
        mapping.append(node)
        depth -= 1

a, b = mapping[X-1], mapping[Y-1]
while depths[a] > depths[b]: a = parents[a]
while depths[b] > depths[a]: b = parents[b]

while a != b:
    a = parents[a]
    b = parents[b]

i = mapping.index(a) + 1
j = mapping.index(a, i) + 1

print(i, j)