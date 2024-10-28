N = int(input())
for _ in range(N):
    arr = input()
    leng = len(arr)
    mid = leng // 2
    doit = arr[mid-1] == arr[mid]
    print("Do-it" if doit else "Do-it-Not")