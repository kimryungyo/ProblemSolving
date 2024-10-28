k = input()

digits = list(map(int, str(k)))

if len(digits) <= 2:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    diff = digits[1] - digits[0]
    for i in range(2, len(digits)):
        if digits[i] - digits[i-1] != diff:
            print("흥칫뿡!! <(￣ ﹌ ￣)>")
            break
    else:
        print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")