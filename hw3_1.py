"""Name: Anthony Francisco
Date: 2/6/23
Title: Wagon Sales - Homework 2 - Programming in Python
Description: This code asks the user to input the number of 
wagons sold in each month of the year (from month 1 to month 12)
 and keeps track of the lowest and highest number of wagons 
 sold in variables called lowest and highest respectively. 
 The code uses a for loop to iterate over the months of the 
 year and the if statement to compare the number of wagons 
 sold on each month to the current value of lowest and highest. 
 If the number of wagons sold on a particular month is lower 
 than the current value of lowest, the value of lowest is 
 updated to reflect the new minimum. If the number of wagons 
 sold on a particular month is higher than the current value 
 of highest, the value of highest is updated to reflect the 
 new maximum. Finally, the code calculates the difference 
 between the highest and lowest number of wagons sold and prints 
 the result."""

# Initialize the variable 'lowest' to keep track of the lowest number of wagons sold
lowest = 1000000
# Initialize the variable 'highest' to keep track of the highest number of wagons sold
highest = 0
# Create a list to store the number of wagons sold in each month
wagon_list = []

# Iterate over the months of the year
for i in range(1,13):
    # Ask the user to input the number of wagons sold in a month
    wagon_count = int(input("Enter the number of wagons sold in month " + str(i) + " : "))
    # Add the number of wagons sold in the current month to the list
    wagon_list.append(wagon_count)

# Iterate over the list of wagons sold in each month
for wagon in wagon_list:
    # Check if the number of wagons sold in the current month is lower than the current value of 'lowest'
    if wagon < lowest:
        # Update the value of 'lowest' if the current number of wagons is lower
        lowest = wagon
    # Check if the number of wagons sold in the current month is higher than the current value of 'highest'
    if wagon > highest:
        # Update the value of 'highest' if the current number of wagons is higher
        highest = wagon

# Calculate the difference between the highest and lowest number of wagons sold
difference = highest - lowest
# Print the difference between the most wagons sold and the least wagons sold
print("The difference between the most wagons sold and the least wagons sold is ", difference)
