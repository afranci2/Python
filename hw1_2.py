homework_grade = float(input("Enter homework grade:"))
midterm_grade = float(input("Enter midterm grade:"))
final_grade = float(input("Enter final grade:"))

homework_weight = .45
midterm_weight = .25
final_weight = .3

calculated_grade = homework_grade * homework_weight + \
    midterm_grade*midterm_weight + final_grade*final_weight

print("Your final grade is: ", calculated_grade)
