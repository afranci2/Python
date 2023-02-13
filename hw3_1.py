lowest=1000000
highest=0
for i in range(1,13):
    wagon_count = int(input("Enter the number of wagons sold in month " + str(i) + " : "))
    if wagon_count<lowest:
        lowest=wagon_count
    if wagon_count>highest:
        highest=wagon_count
difference = highest-lowest
print("The difference between the most wagons sold and the least wagons sold is: ", difference)
