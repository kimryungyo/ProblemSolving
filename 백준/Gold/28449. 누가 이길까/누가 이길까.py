def main():
    import bisect
    left_search = bisect.bisect_left
    right_search = bisect.bisect_right

    N, M = map(int, input().split())

    NS = map(int, input().split())
    MS = sorted(map(int, input().split()))

    N_WINS = M_WINS = SAMES = 0

    for N_S in NS:
        left = left_search(MS, N_S)
        right = right_search(MS, N_S)
        
        SAMES += right - left
        N_WINS += left
        M_WINS += M - right

    print(N_WINS, M_WINS, SAMES)

main()