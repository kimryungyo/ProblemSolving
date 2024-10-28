size = int(input())
block = """
@   @
@   @
@@@@@
@   @
@@@@@
""".strip()

for line in block.split("\n"):
    for _ in range(size):
        for tile in line:
            print(tile * size, end = "")
        print("")