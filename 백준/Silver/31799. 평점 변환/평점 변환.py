total_semester = int(input())
ratings = input()
if ratings[-1] in "ABC": ratings += "0"

ratings_len = len(ratings)
new_ratings = []

semester = 1
previous_rating = None

i = 0
while semester <= total_semester:
    rating = ratings[i] + ratings[i + 1]
    if rating[1] in "ABC": rating, step = rating[0] + "0", 1
    else: step = 2

    if previous_rating == None:
        if rating in "C+, C0, C-": new_ratings.append("B")
        elif rating in "B0, B-": new_ratings.append("D")
        elif rating in "A-, B+": new_ratings.append("P")
        elif rating in "A0, A+": new_ratings.append("E")

    else:
        if rating in "C+, C0, C-": new_ratings.append("B")

        elif rating in "B0, B-":
            if previous_rating in "C+, C0, C-": new_ratings.append("D")
            elif previous_rating in "A+, A0, A-, B+, B0, B-": new_ratings.append("B")

        elif rating in "A-, B+":
            if previous_rating in "B0, B-, C+, C0, C-": new_ratings.append("P")
            elif previous_rating in "A+, A0, A-, B+": new_ratings.append("D")

        elif rating in "A0":
            if previous_rating in "A-, B+, B0, B-, C+, C0, C-": new_ratings.append("E")
            elif previous_rating in "A+, A0": new_ratings.append("P")

        elif rating in "A+": new_ratings.append("E")
    
    previous_rating = rating
    i += step
    semester += 1

print("".join(new_ratings))