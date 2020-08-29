import os
import csv

csvpath = "Resources/budget_data.csv"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    print("Financial Analysis")
    print("---------------------------------------")

    numbermonths = 0
    columnvalue = 0
    for row in csvreader:
        numbermonths += 1
        columnvalue = float(row[1]) + columnvalue

    
        
    
    #listcsvreader = list(csvreader)

    #print(listcsvreader)
    #i = 0
    #change = 0
    #listcolumnvalue = []
    #while i in range(len(listcsvreader)-1):
        #change = float(listcsvreader[i + 1][1]) - float(listcsvreader[i][1])
        #i = i + 1
        #listcolumnvalue.append(change)

    
    #total = 0
    #x = 0
    #while x < len(listcolumnvalue):
        #total = total + listcolumnvalue[x]

   # print(total)
    #print("Total Months:" + str(numbermonths))
    #print("Total:" + str(columnvalue))
   # print(listcolumnvalue)

