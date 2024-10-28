self_numbers = set()
for i in range(1, 10001):
    self_num = i + sum(map(int, str(i)))
    if self_num <= 10000:
        self_numbers.add(self_num)

for i in range(1, 10001):
    if i not in self_numbers:
        print(i)