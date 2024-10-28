A, B, C, D = map(int, input().split())
P, M, N = map(int, input().split())

p_count = 0
if 0 < P % (A + B) <= A:
    p_count += 1
if 0 < P % (C + D) <= C:
    p_count += 1
print(p_count)

m_count = 0
if 0 < M % (A + B) <= A:
    m_count += 1
if 0 < M % (C + D) <= C:
    m_count += 1
print(m_count)

n_count = 0
if 0 < N % (A + B) <= A:
    n_count += 1
if 0 < N % (C + D) <= C:
    n_count += 1
print(n_count)