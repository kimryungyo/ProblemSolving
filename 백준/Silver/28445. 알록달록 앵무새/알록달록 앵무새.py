dad_body, dad_tail = input().split()
mom_body, mom_tail = input().split()

child = []
for body in [dad_body, mom_body, dad_tail, mom_tail]:
    for tail in [dad_body, mom_body, dad_tail, mom_tail]:
        child.append((body, tail))

for body, tail in sorted(set(child)):
    print(body, tail)