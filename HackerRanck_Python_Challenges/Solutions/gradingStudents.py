"""author == "rockefeller"""


def gradingStudents(grades):
    RoundedGrade = []
    for grade in grades:
        if grade < 38:
            RoundedGrade.append(grade)
        elif grade%5 < 3 :
            RoundedGrade.append(grade)
        else:
            RoundedGrade.append(int(round(grade/5 , 0)*5))
    return RoundedGrade
