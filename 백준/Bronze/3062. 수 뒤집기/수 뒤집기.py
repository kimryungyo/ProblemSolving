def is_palindrome(s):
    return s == s[::-1]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N = data[i]
        reversed_N = N[::-1]
        sum_N = str(int(N) + int(reversed_N))
        
        if is_palindrome(sum_N):
            results.append("YES")

        else:
            results.append("NO")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()