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
    target_index=-1
    for i in range(len(list_of_abb)):
        if (list_of_abb[i]==target):
            target_index=i
    if (target_index != -1):
        return list_of_pop[target_index]




def higherPopStates():
    n=1
def printResults():
    n=1

def main():
    list_of_abb, list_of_pop = getStates()
    searchState(list_of_abb, list_of_pop)
    higherPopStates()
    printResults()

main()