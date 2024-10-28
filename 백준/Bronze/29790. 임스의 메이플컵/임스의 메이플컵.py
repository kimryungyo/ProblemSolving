count, union, max = map(int, input().split())
if count >= 1000 and (union >= 8000 or max >= 260): print("Very Good")
elif count >= 1000: print("Good")
else: print("Bad")