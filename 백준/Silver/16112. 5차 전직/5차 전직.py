from sys import stdin
input = lambda: stdin.readline().rstrip()
    
n, k = map(int, input().split())
quests = list(map(int, input().split()))
quests.sort()

exps = 0
stones = 0
for exp in quests:
    exps += exp * stones
    if stones < k: stones += 1
print(exps)