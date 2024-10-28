n = int(input())

members = []
for i in range(n):
    age, name = input().split()
    age = int(age)
    priority = age * 1e10 + i
    members.append((priority, age, name))

members.sort(key=lambda x: x[0])

for member in members:
    print(member[1], member[2])
