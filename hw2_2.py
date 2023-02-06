# Name: Anthony Francisco
# Date: 2/6/23
# Title: CSC 110 - Homework 2 - Programming in Python
# Description: This code calculates the average score for three weeks. 
# It asks the user to input the scores for each week and keeps track of 
# the total score in a variable called accumulator. The code uses a 
# for loop to iterate over the weeks and adds the scores entered to 
# the accumulator. Finally, the code calculates and prints the average 
# score by dividing the accumulator by the number of weeks (9).

# Initialize the accumulator variable to keep track of the total score
accumulator = 0

# Iterate over 9 weeks
for i in range(9):
    # Ask the user to input a score
    score = float(input("Enter score: "))
    
    # Add the score to the accumulator
    accumulator = accumulator + score

# Calculate the average score by dividing the accumulator by 9
average = accumulator / 9

# Round the average to 2 decimal places
rounded_average = round(average, 2)

# Print the average score
print("Your average score for three weeks is: ", rounded_average)

