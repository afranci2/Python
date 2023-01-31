homework_grade = float(input("Enter Homework grade: "))
midterm_grade = float(input("Enter Midterm grade: "))
final_grade = float(input("Enter Final Exam grade: "))


calculated_grade = homework_grade * .45 + midterm_grade*.25 + final_grade*.3

print('Your final grade is: ', round(calculated_grade,2))
