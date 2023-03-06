"""
Name: Anthony Francisco
Date: 3/6/23
Title: CSC 110 - Homework 6 

Description: This program reads a data file containing World Series champions from 1904 to the present and allows users to query the data.

The getData() function opens the file and reads it line by line, storing each piece of information in a separate list (yearList, winnerList, loserList). It then returns the three lists.

The getYears(yearList) function prompts the user to enter two years and returns them if both are valid inputs (i.e., integers within the range of the data).

The percentChange(value1, value2) function takes two values and returns the percent change between them.

The computePercentChange(yearList, totalCSGradsList, menCSGradsList, womenCSGradsList, year1, year2) function calculates the percent change between the total number of CS graduates, the number of male CS graduates, and the number of female CS graduates for the two years given as inputs.

The printResults(totalGradCompute, menCSGrad, womenCSGrad) function takes the percent changes for total graduates, male graduates, and female graduates and prints them to the console.

"""
def getData():
    # This function will get the data from the data file - be sure to look at the format of the data in the
    # file and read each line as we did with the phone search program in class.
    goodFile = False
    while goodFile == False:
        fname = input("Please enter the name of the data file: ")
        try:
            dataFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid file name, try again...")
    #make lists to add data to
    yearList = []
    totalCSGradsList = []
    menCSGradsList = []
    womenCSGradsList = []

    #start reading each line and add to lists
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

#function that asks for year input and validates year input 

def getYears(yearList):
    valid = False
    years = []
    while valid==False:
        while len(years)!= 1:
            year1 = input("Enter a year: ")
            valid=True
            if year1.isdigit() == False:
                print("Invalid entry, try again...")
                valid = False
            elif int(year1) not in yearList or int(year1)==1971:
                print("Year not in range, try again...")
                valid = False
            if valid==True:
                year1=int(year1)
                years.append(year1)
    return years[0]

 #function that calculates and returns percentchange

def percentChange(value2, value1):
    return ((value2-value1)/value1)

 #function that will compute the percent change of three values by the user inpute

def computePercentChange(year1, yearList, womenCSGradsList):
    index1=0
    for i in range(len(yearList)):
        if year1 == (yearList[i]):
            index1=i
        #uses previous function to computer perent change
    womenCSGrad =percentChange(int(womenCSGradsList[index1-1]),int(womenCSGradsList[index1]))
    return womenCSGrad
    
def outputFile(year1, womenCSGradsList, yearList):
    outname = "womenGradChangeFrom"+str(year1)+".csv"
    found=False
    outFile = open(outname, 'w')
    while year1 <=2011:
        outFile.write(str(year1)+","+str(computePercentChange(year1, yearList, womenCSGradsList))+ "\n")
        found=True
        year1=year1+1
    print("Your data has been written to the file ", outname)
#main function to call previous functions

def main():    
    # Call the function to get the data from the data file and store the results in three lists
    yearList,totalCSGradsList,menCSGradsList,womenCSGradsList = getData()
    year1= getYears(yearList)
    outputFile(year1, womenCSGradsList, yearList)
