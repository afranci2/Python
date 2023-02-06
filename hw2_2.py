for i in range(9):
    accumulator = 0
    score = float(input("Enter score: "))
    accumulator += score
print("Your average score for the three weeks is: ", "{:,2f}".format(accumulator))
