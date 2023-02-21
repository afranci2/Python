def getStates():
    NumberOfStates = int(input("How many states are in your list? "))
    list_of_abb = []
    list_of_pop=[]
    for i in range(NumberOfStates):
        state_abb = input("Enter state abbreviation: ")
        list_of_abb.append(state_abb)
        state_pop = int(input("Enter state population: "))
        list_of_pop.append(state_pop)
    return list_of_abb, list_of_pop

def searchState(list_of_abb, list_of_pop):
    target = input("Enter a state to find population of: ")
    for i in range(len(list_of_abb)):
        if (list_of_abb[i]==target):
            return i
    return -1

def higherPopStates(list_of_abb, list_of_pop, state_index):
    list_of_higher_states=[]
    for i in range(len(list_of_pop)):
        if (list_of_pop[i]>list_of_pop[state_index]):
            list_of_higher_states.append(list_of_abb[i])
    return list_of_higher_states

def printResults(list_of_abb, list_of_pop, state_index, higher_state_results):
    print("The states with a higher population than", list_of_abb[state_index], "are: ", higher_state_results)

def main():
    list_of_abb, list_of_pop = getStates()
    state_index = searchState(list_of_abb, list_of_pop)
    higher_state_results = higherPopStates(list_of_abb, list_of_pop, state_index)
    printResults(list_of_abb, list_of_pop, state_index, higher_state_results)