while True:
    a0 = input()
    if a0 == '0': break
    
    unique_nums = set()
    
    while a0 not in unique_nums:
        unique_nums.add(a0)
        a0 = str(int(a0) ** 2).zfill(8)[2:6]
    
    print(len(unique_nums))