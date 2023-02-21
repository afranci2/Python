"""
Name: Anthony Francisco
Date: 2/21/23
Title: CSC 110 - Homework 4 - Programming in Python
Description: The sumDigits() function takes a single 
integer user_number as an input and returns the sum of its
 digits. The function first converts the input user_number 
 to a string called new_number so that each digit can be 
 accessed separately using an index in the following loop.
In the loop, total_sum is initialized to 0 and iterates over
 each character in new_number. It extracts each digit from
  the string by using the index i and converts it back to
  an integer using int(), then adds it to total_sum.
Finally, the function returns the total_sum which is the 
sum of all the digits in user_number.

"""

def sumDigits(user_number):
    # Convert user input to a string so that we can loop through each digit
    new_number = str(user_number)
    
    # Initialize a variable to hold the sum of the digits
    total_sum = 0
    
    # Loop through each digit in the user input and add it to the total sum
    for i in range(len(new_number)):
        # Convert the digit back to an integer and add it to the sum
        total_sum += int(new_number[i])
    
    # Return the final sum of the digits
    return total_sum

def sumDivisible(user_input):
    result = sumDigits(user_input)
    if (user_input%result==0):
        return True
    else:
        return False
