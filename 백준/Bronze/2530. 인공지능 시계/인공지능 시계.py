h, m, s = map(int, input().split())
t = int(input())
total_secs = h * 3600 + m * 60 + s + t
eh = (total_secs // 3600) % 24
em = (total_secs % 3600) // 60
es = total_secs % 60
print(eh, em, es)