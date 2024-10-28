inputed = ''
while True:
    try: inputed += input()
    except: break
        
print(sum(map(int, inputed.split(','))))