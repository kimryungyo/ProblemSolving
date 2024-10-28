import sys
def flush(): sys.stdout.flush()

def ask(name):
    print(f"? {name}")
    flush()
    return int(input())

def answer(name):
    print(f"! {name}")
    flush()
    quit()

N = int(input())
names = [input().strip() for _ in range(N)]

answers = [ 0 ] * N
for i in range(N):
    name = names[i]
    answers[i] += ask(name)
    answers[i] += ask(name)
    if answers[i] == 2: answer(name)

name = names[answers.index(1)]
answer(name)