def computegrade(score):
    try:
        score = float(score)
        if score<0.0 or score>1.0:
            grade = "Bad score"
        else:
            if score>=0.9:
                grade = "A"
            elif score>=0.8:
                grade = "B"
            elif score>=0.7:
                grade = "C"
            elif score>=0.6:
                grade = "D"
            else:
                grade = "F"
    except:
        grade = "Bad score"

    return grade

score = input("Enter score: ")
grade = computegrade(score)

print(grade)