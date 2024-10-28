def check_isbn(isbn):
    total = 0
    for i in range(12):
        if isbn[i] != '*':
            total += int(isbn[i]) * (1 if i % 2 == 0 else 3)
    return (10 - (total % 10)) % 10

isbn = input()
damaged_position = isbn.index('*')
for i in range(10):
    test_isbn = isbn[:damaged_position] + str(i) + isbn[damaged_position+1:]
    if check_isbn(test_isbn) == int(isbn[-1]):
        print(i)
        break