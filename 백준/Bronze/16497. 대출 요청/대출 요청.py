from heapq import heappop, heappush
from sys import stdin
input = lambda: stdin.readline().rstrip()

N = int(input())
events = []
for _ in range(N):
    loan, returns = map(int, input().split())
    events.append( (loan, returns) )
    
loan_list = []
book_count = int(input())

events.sort()
for event in events:
    date, returns = event

    while True:
        if not loan_list: break
        if loan_list[0] <= date:
            heappop(loan_list)
            book_count += 1
        else: break

    if book_count < 1: print(0);quit()
    book_count -= 1
    heappush(loan_list, returns)

print(1)