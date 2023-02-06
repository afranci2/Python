accumulator = 0

for i in range(9):
    score = float(input("Enter score: "))
    accumulator = accumulator+score
    print(accumulator)
print("Your average score for the three weeks is: ", accumulator/9)
