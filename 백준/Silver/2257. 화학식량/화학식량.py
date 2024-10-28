stack = []

formula = input()
for char in formula:
    if char == '(': stack.append("(")
    elif char == 'H': stack.append(1)
    elif char == 'C': stack.append(12)
    elif char == 'O': stack.append(16)

    elif char.isdigit():
        temp = stack[-1] * (int(char) - 0)
        stack.pop()
        stack.append(temp)

    else:
        num = 0
        while stack[-1] != "(":
            num += stack[-1]
            stack.pop()
        stack.pop()
        stack.append(num)

print(sum(stack))