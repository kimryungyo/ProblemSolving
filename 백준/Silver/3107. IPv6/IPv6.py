ip_v6 = input()

group_count = ip_v6.count(":") + 1

while group_count > 8:
    ip_v6 = ip_v6.replace("::", ":", 1)
    group_count -= 1

while group_count < 8:
    ip_v6 = ip_v6.replace("::", ":::", 1)
    group_count += 1

groups = ip_v6.split(":")
restored = []
for group in groups:
    if group == "":
        restored.append("0000")
    else:
        restored.append(group.zfill(4))
        
print(":".join(restored))