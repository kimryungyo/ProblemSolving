import sys, math
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):

    n, m = map(int, input().split())
    cars = {}

    for _ in range(n):
        parts = input().split()
        car, p, q, k = parts[0], int(parts[1]), int(parts[2]), int(parts[3])
        cars[car] = (p, q, k)

    events = []
    for _ in range(m):
        parts = input().split()
        t = int(parts[0])
        spy = parts[1]
        e = parts[2]
        
        if e == 'p':
            car = parts[3]
            events.append((t, spy, e, car))

        elif e == 'r':
            d = int(parts[3])
            events.append((t, spy, e, d))

        elif e == 'a':
            s = int(parts[3])
            events.append((t, spy, e, s))

    events.sort(key=lambda x: x[0])
    spies = defaultdict(lambda: {'car': None, 'cost': 0, 'invalid': False})
    spy_names_set = set()

    for event in events:
        t, spy, e = event[0], event[1], event[2]
        spy_names_set.add(spy)

        if spies[spy]['invalid']:
            continue

        if e == 'p':
            car = event[3]
            if spies[spy]['car'] is not None or car not in cars:
                spies[spy]['invalid'] = True
            else:
                spies[spy]['car'] = car
                spies[spy]['cost'] += cars[car][1]

        elif e == 'r':
            distance = event[3]
            if spies[spy]['car'] is None:
                spies[spy]['invalid'] = True
            else:
                car = spies[spy]['car']
                spies[spy]['cost'] += cars[car][2] * distance
                spies[spy]['car'] = None

        elif e == 'a':
            s = event[3]
            if spies[spy]['car'] is None:
                spies[spy]['invalid'] = True
            else:
                car = spies[spy]['car']
                damage = math.ceil(cars[car][0] * s / 100)
                spies[spy]['cost'] += damage
                
    spy_names = sorted(spy_names_set)

    for spy in spy_names:
        state = spies[spy]
        if state['invalid'] or state['car'] is not None:
            print(f"{spy} INCONSISTENT")
        else:
            print(f"{spy} {state['cost']}")