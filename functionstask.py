# Write a python program that takes from a user 5 inputs
# (maths, eng, swa, sci, sos).
# Create a function that calculates the total marks
#  another the average marks ,then a functions that
# finds the grade according to the table below.
# Use the value from total to get the average and
# average to find the grade.
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40


def find_total_marks(math, eng, kis, sci, sos):
    total = math + eng + kis + sci+sos
    return total


def find_avg_marks(total):
    avg = total / 5
    return avg


def find_grade(avg_marks):
    if avg_marks > 79:
        grade = "A"
    elif avg_marks >= 60 and avg_marks <= 79:
        grade = "B"
    elif avg_marks > 49 and avg_marks <= 59:
        grade = "C"
    elif avg_marks >= 40 and avg_marks <= 49:
        grade = "D"
    else:
        grade = "E"
    return grade


math = int(input("Maths: "))
eng = int(input("English: "))
kis = int(input("Kiswahili: "))
sci = int(input("Science: "))
sos = int(input("Social Studies: "))

total = find_total_marks(math, eng, kis, sci, sos)
avg_marks = find_avg_marks(total)
grade = find_grade(avg_marks)


print("The total is: " + str(total))
print("The avarage marks is: " + str(avg_marks))
print("Grade: " + str(grade))
