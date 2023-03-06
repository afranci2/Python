# World Series Results

# Given a file with the World Series Champions since 1904
# Allow user to ask various questions about the results

def getData():
    # This function will get the data from the data file - be sure to look at the format of the data in the
    # file and read each line as we did with the phone search program in class.
    # The function should return the list of years, the list of winners and the list of losers
    goodFile = False
    while goodFile == False:
        fname = input("Please enter the name of the data file: ")
        try:
            dataFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid file, please try again...")
            print(IOError)
    yearList = []
    totalCSGradsList = []
    menCSGradsList = []
    womenCSGradsList = []


    line = dataFile.readline()
    line = dataFile.readline()
    while line != "":
        line = line.strip()
        year, totalCSGrads, menCSGrads, womenCSGrads = line.split(",")
        yearList.append(int(year))
        totalCSGradsList.append(int(totalCSGrads))
        menCSGradsList.append(int(menCSGrads))
        womenCSGradsList.append(int(womenCSGrads))
        line = dataFile.readline()
    dataFile.close()
    return (yearList,totalCSGradsList,menCSGradsList,womenCSGradsList)

def getYears(yearList):
    valid = False
    years = []
    while valid==False:
        while len(years)!= 2:
            year1 = input("Enter a year: ")
            valid=True
            if year1.isdigit() == False:
                print("Invalid entry, try again...")
                valid = False
            year1=int(year1)
            if year1 not in yearList and valid!=False:
                print("Year not in range, try again...")
                valid = False
            if valid==True:
                years.append(year1)
        valid=True
        if years[0]>years[1]:
                print("year2 should be after year2, try again...")
                valid=False
                years=[]
    
    return years[0], years[1]

def percentChange(value1, value2):
    return ((value2-value1)/value1)*100

def computePercentChange(yearList,totalCSGradsList,menCSGradsList,womenCSGradsList, year1, year2):
    index1=0
    index2=0
    for i in range(len(yearList)):
        if year1 == (yearList[i]):
            index1=i
        if year2 == (yearList[i]):
            index2=i
    totalGradCompute = percentChange(int(totalCSGradsList[index1]),int(totalCSGradsList[index2]))
    menCSGrad = percentChange(int(menCSGradsList[index1]),int(menCSGradsList[index2]))
    womenCSGrad =percentChange(int(womenCSGradsList[index1]),int(womenCSGradsList[index2]))
    
    return totalGradCompute, menCSGrad, womenCSGrad
    
def printResults(totalGradCompute, menCSGrad, womenCSGrad):
    print("Percent change overall: ", round(totalGradCompute, 2), "%")
    print("Percent change men: ", round(menCSGrad, 2), "%")
    print("Percent change women: ", round(womenCSGrad, 2), "%")

def main():    
    # Call the function to get the data from the data file and store the results in three lists
    yearList,totalCSGradsList,menCSGradsList,womenCSGradsList = getData()
    year1, year2 = getYears(yearList)
    totalGradCompute, menCSGrad, womenCSGrad = computePercentChange(yearList,totalCSGradsList,menCSGradsList,womenCSGradsList, year1, year2)
    printResults(totalGradCompute, menCSGrad, womenCSGrad)
