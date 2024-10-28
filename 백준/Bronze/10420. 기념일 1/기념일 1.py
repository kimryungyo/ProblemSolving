n = int(input())
year, month, day = 2014, 4, 2

n -= 1
while n > 0:
    day += 1
    if month in [1, 3, 5, 7, 8, 10] and day == 32:
        month += 1
        day = 1
    elif month in [4, 6, 9, 11] and day == 31:
        month += 1
        day = 1
    elif month == 12 and day == 32:
        year += 1
        month = 1
        day = 1
    elif month == 2:
        c = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
        if (day == 29 and not c) or (day == 30 and c):
            month += 1
            day = 1
    n -= 1

print(f"{year}-{month:02d}-{day:02d}")