from sys import stdin
input = lambda: stdin.readline().rstrip()

N = int(input())
mentors = {}

for _ in range(N):
    mento, mentee = input().split()
    if mento not in mentors:
        mentors[mento] = []
    mentors[mento].append(mentee)

for mentor in sorted(mentors.keys()):
    mentees = sorted(mentors[mentor], reverse=True)
    for mentee in mentees:
        print(mentor, mentee)