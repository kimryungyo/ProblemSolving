def P5(students):
    from fractions import Fraction

    def scans(observer, others):
        max = Fraction(others[0] - observer, 1)
        count = 1
        dist = 0
        for other in others:
            dist += 1
            slope = Fraction(other - observer, dist)
            if slope > max:
                count += 1
                max = slope
        return count

    max_count = 0

    for i in range(len(students)):
        observer = students[i]

        count = 0
        
        if i > 0:
            count += scans(observer, students[:i][::-1])

        if i < len(students) - 1:
            count += scans(observer, students[i+1:])

        if count > max_count:
            max_count = count

    return max_count