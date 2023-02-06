accumulator = 0

for i in range(9):
    score = float(input("Enter score: "))
    accumulator = accumulator+score
print("Your average score for three weeks is: ", round(accumulator/9,2))
