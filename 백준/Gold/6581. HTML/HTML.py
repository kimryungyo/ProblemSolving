stack = 0
for line in open(0).read().split():
    words = line.split()

    for word in words:
        if word == "<br>":
            stack = 0
            print()

        elif word == "<hr>":
            if stack:
                stack = 0
                print()

            print("-" * 80)

        else:
            if stack + len(word) + 1 > 80:
                stack = 0
                print()

            if stack:
                print(" ", end="")
                stack += 1
                
            print(word, end="")
            stack += len(word)
