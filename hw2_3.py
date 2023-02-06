"""
Name: Anthony Francisco
Date: 2/6/23
Title: CSC 110 - Homework 2 - Programming in Python
Description: This code asks the user to input 
the number of bugs collected on each day of the week 
(from day 1 to day 7) and keeps track of the highest number
 of bugs collected in a variable called highest. The code 
 uses a for loop to iterate over the days of the week 
 and the if statement to compare the number of bugs 
 collected on each day to the current value of highest. 
 If the number of bugs collected on a particular day is greater 
 than the current value of highest, the value of highest is updated 
 to reflect the new maximum. Finally, the code prints the highest number 
 of bugs collected during the week.

"""

# Initialize the variable 'highest' to keep track of the highest number of bugs collected
highest = 0

# Iterate over the days of the week
for i in range(1, 8):
    # Ask the user to input the number of bugs collected on a day
    bug = int(input("How many bugs did you collect on day {}: ".format(i)))
    
    # Check if the number of bugs collected on the current day is greater than the current value of 'highest'
    if bug > highest:
        # Update the value of 'highest' if the current number of bugs is greater
        highest = bug

# Print the highest number of bugs collected during the week
print("The highest number of bugs collected this week is ", highest)

