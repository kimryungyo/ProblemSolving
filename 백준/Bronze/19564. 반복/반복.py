string = input()

count = 1
for i in range(len(string) - 1):
    if ord(string[i]) >= ord(string[i+1]): 
        count += 1

print(count)