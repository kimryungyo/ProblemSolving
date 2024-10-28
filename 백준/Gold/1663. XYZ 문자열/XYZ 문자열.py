question = int(input())
n = int(input())

if (question == 1) or (question == 3):
    count = {"X": 1, "Y": 0, "Z": 0}
    for _ in range(n - 1): count = { "X": count["Z"], "Y": count["X"], "Z": count["X"] + count["Y"] }

    if question == 1: print(sum(count.values()))
    else: print(count[input()])

else:
    target = int(input())

    string = "X"
    depth = 1

    count = {"X": 0, "Y": 0, "Z": 0}
    total_count = 0

    for i in range(n - 1):
        depth += 1

        if string == "Y": string = "Z"
        elif string == "Z": string = "X"
        else:

            y_count = {"X": 0, "Y": 1, "Z": 0}
            for _ in range(n - depth): y_count = { "X": y_count["Z"], "Y": y_count["X"], "Z": y_count["X"] + y_count["Y"] }
            y_total_count = sum(y_count.values())

            if (total_count + y_total_count) < target: 
                count = { "X": count["X"] + y_count["X"], "Y": count["Y"] + y_count["Y"], "Z": count["Z"] + y_count["Z"] }
                total_count = total_count + y_total_count
                string = "Z"
            else: string = "Y"

    print(string)