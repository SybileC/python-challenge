import os
import csv

#Find path to file
csvpath = "Resources/budget_data.csv"

#open file and use the reader object to read it
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#Use next() function to skip file's header
    next(csvreader)

#Print Header
    Header = "Financial Analysis"
    print(Header)
    print("---------------------------------------")

#Assign variables and list 
    numbermonths = 0
    columnvalue = 0
    listchanges = []
    change = 0
    rowcount = 0

#Use for loop to go through each row and add values to each variable and to the list
    for row in csvreader:
#Add each line to determine the number of months
        numbermonths += 1
#Add the value of each row from second column to get total loss/Profit
        columnvalue = float(row[1]) + columnvalue 
#Subtract change from first row in second column
        change = float(row[1]) - change
#Set rowcount to repeat subtract with each row
        rowcount += 1
#Store results in list
        listchanges.append(change)   

#Calculate average change by dividing the difference between the change in the last month and first month and the number of months minus 1 
    averagechange = round((listchanges[85] - listchanges[0]) / (numbermonths - 1), 2)

#Use max() and min() functions to find the lowest and highest value in listchanges
    greatestincrease = max(listchanges)
    greatestdecrease = min(listchanges)

#Print results and convert them to string to concatenate them with other strings 
    print("Total Months:" + "  " + str(numbermonths))
    print("Total:" + "  " + "$" + str(columnvalue))
    print("Average Change:" + "  " + "$" + str(averagechange))
    print("Greatest Increase in Profits:" + "  " + "$" + str(greatestincrease))
    print("Greatest Decrease in Profits:" + "  " + "$" + str(greatestdecrease))

#Create output path for csv file to be created
outputfile = "Analysis/PyBank.csv"

#Create 2 lists (The variables and the values assigned to them)
variables = ["Total Months", "Total", "Average Change", "Greatest Increase in Profits", "Greatest Decrease in Profits"]
values = [numbermonths, columnvalue, averagechange, greatestincrease, greatestdecrease]

#Use zip function to combine the 2 lists
pybank = zip(variables, values)

#Open output file and use the writer object to edit file
with open(outputfile, 'w') as datafile:
    csvwriter = csv.writer(datafile)

#Print rows 
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerows(pybank)
    

