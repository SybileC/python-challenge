import os
import csv

csvpath = os.path.join("C:/Users/Babyta/Desktop/Columbia BCS", "budget_data.csv")

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
    
    print("Total Months:" + str(numbermonths))
    print("Total:" + str(columnvalue))   
    
    listcsvreader = list(csvreader)
    i = 0
    change = 0
    listcolumnvalue = []
    while i in range(len(listcsvreader)-1):
        change = float(listcsvreader[i + 1][1]) - float(listcsvreader[i][1])
        i = i + 1
        listcolumnvalue.append(change)

    print(listcolumnvalue)
    #print(change)
    
    

    
    
    
    
    #listcsvreader = list(csvreader)
    
    #print(listcsvreader)

    #print(listcsvreader[0][1])

    #change = float(listcsvreader[1][0]) - float(listcsvreader[0][0])
    
    #i = 0 
    #change = listcsvreader[1][1] - listcsvreader[0][1]
    #While i < len(listcsvreader):
        #Change = listcsvreader[i][1] listcsvreader[i][1]

   #print(change)

    
    
    
    
    #change = listcsvreader[i +1][1] - listcsvreader[i][1]
    
    
    
    
    
    #i = 0
    #listcolumnvalue = []
    #for listcsvreader[i][1] in listcsvreader:
        #change = listcsvreader[i + 1][1] - listcsvreader[i][1]
    
    #listcolumnvalue = listcolumnvalue.append(change)
    
   
   
   
   
    #list = []
    #listcolumnvalue = list.append(row[1])


 
    
    #print("Average Change:" + str(average))
    #print("Greatest Decrease in Profits:" + str(minvalue))
    #print(listcolumnvalue)


    #average = totalprofitloss / numbermonths

    #

    #listcolumnvalue = []
    #for columnvalue in csvreader:
        #listcolumnvalue.insert(columnvalue)
        #minvalue = min(listcolumnvalue)
        #maxvalue = max(listcolumnvalue)

    #print("Greatest Increase in Profits:" + str(maxvalue))
    #print("Greatest Decrease in Profits:" + str(minvalue))

#listcolumnvalue = []
        #minvalue = min(listcolumnvalue)