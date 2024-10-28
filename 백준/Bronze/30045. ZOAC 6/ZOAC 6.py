n = int(input())
count = 0
for i in range(n):
    line = input()
    if "01" in line:
        count += 1
        continue
    if "OI" in line:
        count += 1
        continue
print(count)