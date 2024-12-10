import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
Q_A_pairs = [ tuple(input().split()) for _ in range(N) ]
sentences = [ input() for _ in range(M) ]

sorted_QA = sorted(Q_A_pairs, key=lambda x: x[0])

for sentence in sentences:
    result = []
    len_S = len(sentence)
    for k in range(len_S):
        for Q, A in sorted_QA:
            len_Q = len(Q)
            if k + len_Q <= len_S and sentence[k:k+len_Q] == Q:
                result.append(A)
    
    print("".join(result) if result else -1)