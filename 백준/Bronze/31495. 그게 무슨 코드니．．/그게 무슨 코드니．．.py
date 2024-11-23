string = input()
if len(string) < 3:
    print("CE")
elif string[0] == '"' and string[-1] =='"':
    print(string[1:-1])
else: 
    print("CE")