"""
Name: Anthony Francisco
Date: 2/21/23
Title: CSC 110 - Homework 4 - Programming in Python
Description: This program asks the user to input a list of states and their populations.
It then prompts the user to input a state abbreviation to find the population of,
and outputs the population of that state as well as the states with a higher population.
"""

def getStates():
# Prompts user to input the number of states and their populations, and returns a tuple
    NumberOfStates = int(input("How many states are in your list? "))
    list_of_abb = []
    list_of_pop=[]
    for i in range(NumberOfStates):
        state_abb = input("Enter state abbreviation: ")
        list_of_abb.append(state_abb)
        state_pop = int(input("Enter state population: "))
        list_of_pop.append(state_pop)
    return list_of_abb, list_of_pop

def searchState(list_of_abb, target):
# Searches the list of state abbreviations for a target state and returns its index
    target_index=-1
    for i in range(len(list_of_abb)):
        if (list_of_abb[i]==target):
            target_index = i
    if (target_index == -1):
        print("The state you entered is not valid")
        return -1
    else:
        return target_index

def higherPopStates(list_of_abb, list_of_pop, state_index):
    # Creates a list of states with a higher population than the target state
    list_of_higher_states=[]
    for i in range(len(list_of_pop)):
        if (list_of_pop[i]>list_of_pop[state_index]):
            list_of_higher_states.append(list_of_abb[i])
    return list_of_higher_states

def printResults(list_of_abb, state_index, list_of_pop, higher_state_results):
# Prints the population of the target state and the list of states with a higher population
    print("The population of ", list_of_abb[state_index], "is", list_of_pop[state_index])
    print("The states with a higher population than", list_of_abb[state_index], "are:", higher_state_results)

def main():
    # Calls the getStates() function and assigns its tuple elements to two separate lists
    list_of_abb, list_of_pop = getStates()
    # Prompts user to input a state abbreviation to search for
    target = input("Enter a state to find population of: ")
    # Calls the searchState() function to find the index of the target state abbreviation in the list
    state_index = searchState(list_of_abb, target)
    if(state_index != -1):
        # Calls the higherPopStates() function to create a list of states with a higher population than the target state
        higher_state_results = higherPopStates(list_of_abb, list_of_pop, state_index)
        # Calls the printResults() function to output the population of the target state and the list of states with a higher population
        printResults(list_of_abb, state_index, list_of_pop, higher_state_results)
