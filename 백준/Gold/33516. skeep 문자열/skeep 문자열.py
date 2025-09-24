n = int(input())
string = input()

def check(stack):
    if len(stack) < 5: return False
    key = "skeep"
    for i in range(-1, -6, -1):
        char = stack[i]
        if char == "*" and key[i] != "s": continue
        if char != key[i]: return False
    return True

count = 0
stack = []
for char in string:
    stack.append(char)
    while check(stack):
        del stack[-5:]
        stack.append("*")
        count += 1

print(count)