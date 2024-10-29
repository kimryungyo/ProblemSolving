S = input()

print(" ".join(map(str, [S.find(x) for x in 'abcdefghijklmnopqrstuvwxyz'])))