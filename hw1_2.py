homework_grade = float(input("Enter Homework grade: "))
midterm_grade = float(input("Enter Midterm grade: "))
final_grade = float(input("Enter Final grade: "))

homework_weight = .45
midterm_weight = .25
final_weight = .3

calculated_grade = homework_grade * homework_weight + \
    midterm_grade*midterm_weight + final_grade*final_weight

print('Your final grade is', round(final_grade,2))
