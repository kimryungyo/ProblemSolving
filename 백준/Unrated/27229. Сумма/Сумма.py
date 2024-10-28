from sys import stdout, setrecursionlimit
setrecursionlimit(10 ** 5)
print = stdout.write

N = int(input())
K = int(input())

def dfs(stack: list, sum: int):
    if len(stack) == K:
        if sum == N:
            print(str(stack[0]))
            for i in range(1, len(stack)):
                num = stack[i]
                if num >= 0: print("+")
                print(str(num))
            print("\n")

        return None

    last = stack[-1]
    
    for i in range(last - 1, last + 2):
        stack.append(i)
        dfs(stack, sum + i)
        stack.pop()

for i in range(-15, 16):
    stack = [i]
    dfs(stack, i)