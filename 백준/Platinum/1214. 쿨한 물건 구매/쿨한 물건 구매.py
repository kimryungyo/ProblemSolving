price, bill_1, bill_2 = map(int, input().split())

min_bill, max_bill = sorted([bill_1, bill_2])
if price % min_bill == 0 or price % max_bill == 0:
    print(price)
    quit()

min_count = price // max_bill
min_payment = max_bill * (min_count + 1)

for max_count in range(min_count, -1, -1):

    div, mod = divmod(price - (max_count * max_bill), min_bill)
    if mod == 0: print(price); quit()

    payment = max_count * max_bill + ((div + 1) * min_bill)
    if payment == min_payment: break
    elif price <= payment < min_payment:
        min_payment = payment

print(min_payment)