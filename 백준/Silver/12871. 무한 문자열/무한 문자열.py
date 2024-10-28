s = input()
t = input()

loop_s = s * 512
loop_t = t * 512

if loop_s[:500] == loop_t[:500]: print(1)
else: print(0)