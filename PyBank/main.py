import os
import csv

#Find path to file
csvpath = "Resources/budget_data.csv"

#open file and use the reader object to read it
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#Use next() function to skip file's header
    next(csvreader)

    print("Financial Analysis")
    print("---------------------------------------")

#Assign variables to 
    numbermonths = 0
    columnvalue = 0
    listchanges = []
    change = 0
    rowcount = 0
    for row in csvreader:
        numbermonths += 1
        columnvalue = float(row[1]) + columnvalue 
        change = float(row[1]) - change
        rowcount += 1
        listchanges.append(change)   

    averagechange = (listchanges[85] - listchanges[0]) / (numbermonths - 1)

    highestincrease = max(listchanges)
    lowestdecrease = min(listchanges)

    print("Total Months:" + "  " + str(numbermonths))
    print("Total:" + "  " + str(columnvalue))
    print(str(listchanges))
    print("Average Change:" + "  " + str(averagechange))
    print("Greatest Increase in Profits:" + "  " + str(highestincrease))
    print("Greatest Decrease in Profits:" + "  " + str(lowestdecrease))
        
    

