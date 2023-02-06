# Name: Anthony Francisco
# Date: 2/6/23
# Title: CSC 110 - Homework 2 - Programming in Python
# Description: This code calculates the average score for three weeks. 
# It asks the user to input the scores for each week and keeps track of 
# the total score in a variable called accumulator. The code uses a 
# for loop to iterate over the weeks and adds the scores entered to 
# the accumulator. Finally, the code calculates and prints the average 
# score by dividing the accumulator by the number of weeks (9).

# Initialize the variable 'accumulator' to keep track of the total score
accumulator = 0

# Iterate over the weeks
for i in range(9):
    # Ask the user to input the score for a week
    score = float(input("Enter score for week {}: ".format(i+1)))
    
    # Add the score for the current week to the accumulator
    accumulator = accumulator + score

# Calculate the average score for three weeks
average_score = accumulator / 9

# Print the average score rounded to 2 decimal places
print("Your average score for three weeks is: ", round(average_score, 2))
