from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
table = set()

for _ in range(n):
    cmd = input()

    if cmd == "all":
        table = { i for i in range(1, 20 + 1) }
    
    elif cmd == "empty":
        table = set()

    else:
        cmd, value = cmd.split()
        value = int(value)

        if cmd == "add":
            table.add(value)

        elif cmd == "remove":
            if value in table:
                table.remove(value)

        elif cmd == "toggle":
            if value in table:
                table.remove(value)
            else:
                table.add(value)

        else:
            if value in table:
                print(1)
            else:
                print(0)