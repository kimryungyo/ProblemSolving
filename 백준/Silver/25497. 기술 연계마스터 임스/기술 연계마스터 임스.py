N = int(input())
skills = input()

normal_skills = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
L, S = 0, 0
count = 0
for skill in skills:
    if skill in normal_skills:
        count += 1
        continue

    if skill == "L": 
        L += 1
        continue

    if skill == "R":
        if L:
            L -= 1
            count += 1
        else: break

    if skill == "S": 
        S += 1
        continue

    if skill == "K":
        if S:
            S -= 1
            count += 1
        else: break

print(count)