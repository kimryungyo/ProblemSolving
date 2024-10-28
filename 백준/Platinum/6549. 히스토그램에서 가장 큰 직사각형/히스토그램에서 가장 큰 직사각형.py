from sys import stdin
input = lambda: stdin.readline().rstrip()

def getMidArea(lo, hi, mid):
    toLeft = mid
    toRight = mid
    height = histogram[mid]
    maxArea = height
    
    while lo < toLeft and toRight < hi:
        if histogram[toLeft - 1] < histogram[toRight + 1]:
            toRight += 1
            height = min(height, histogram[toRight])
        else:
            toLeft -= 1
            height = min(height, histogram[toLeft])
        
        maxArea = max(maxArea, height * (toRight - toLeft + 1))
    
    while toRight < hi:
        toRight += 1
        height = min(height, histogram[toRight])
        maxArea = max(maxArea, height * (toRight - toLeft + 1))
    
    while lo < toLeft:
        toLeft -= 1
        height = min(height, histogram[toLeft])
        maxArea = max(maxArea, height * (toRight - toLeft + 1))
    
    return maxArea

def getArea(lo, hi):
    if lo == hi: return histogram[lo]
    
    mid = (lo + hi) // 2
    leftArea = getArea(lo, mid)
    rightArea = getArea(mid + 1, hi)
    maxArea = max(leftArea, rightArea)
    maxArea = max(maxArea, getMidArea(lo, hi, mid))
    
    return maxArea

while True:
    n, *histogram = map(int, input().split())
    if not histogram: break
    print(getArea(0, n - 1))