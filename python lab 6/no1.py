def cal_grade(mark):
    if 80 <= mark <= 100:
        grade = "A"
    elif 70 <= mark < 80:
        grade = "B"
    elif 60 <= mark < 70:
        grade = "C"
    elif 50 <= mark < 60:
        grade = "D"
    elif 0 <= mark < 50:
        grade = "F"
    else:
        grade = "Error"
    return grade

inputMark = int(input("Enter your mark: "))
print(cal_grade(inputMark))
