"""Name: Anthony Francisco
Date: 2/6/23
Title: CSC 110 - Homework 2 - Programming in Python
Description: This code asks the user for the number of ages that 
have been collected. Then it prompts the user to input each age. 
The ages are stored in a list called 'age_list'. The code then uses 
a for loop to iterate through the 'age_list' and append every third 
age to a new list called 'sampled_list'. Finally, the code prints 
the 'sampled_list' which contains every third age from the original 'age_list'.
"""

# Initialize empty list to store ages
age_list = []

# Initialize empty list to store sampled ages
sampled_list = []

# Ask the user for the number of ages that have been collected
age_count = int(input("How many ages have been collected? "))

# Loop to input each age and append to 'age_list'
for i in range(age_count):
    # Ask the user to input an age
    age = int(input("Enter age: "))
    # Append the age to the 'age_list'
    age_list.append(age)

# Loop to iterate through 'age_list' and append every third age to 'sampled_list'
for i in range(len(age_list)):
    # Check if the current index is a multiple of 3
    if i%3==0:
        # Append the age at the current index to 'sampled_list'
        sampled_list.append(age_list[i])

# Print the 'sampled_list'
print("The sampled list is: " , sampled_list)
