from sys import stdin
input = lambda: stdin.readline().rstrip()

string = input()

i = 0
while i < len(string):
    sub_str = string[i:i+2]

    if sub_str in {"pi", "ka"}:
        i += 2
        continue

    sub_str = string[i:i+3]
    if sub_str == "chu":
        i += 3
        continue

    print("NO")
    quit()

print("YES")