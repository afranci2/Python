lowest=1000000
highest=0
wagon_list = []
for i in range(1,13):
    wagon_count = int(input("Enter the number of wagons sold in month " + str(i) + " : "))
    wagon_list.append(wagon_count)
for wagon in wagon_list:
    if wagon<lowest:
            lowest=wagon_count
    if wagon>highest:
            highest=wagon_count
difference = highest-lowest
print("The difference between the most wagons sold and the least wagons sold is ", difference)
