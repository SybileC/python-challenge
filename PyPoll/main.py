import os
import csv

csvpath = os.path.join("C:/Users/Babyta/Desktop/Columbia BCS", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=(','))

    next(csvreader)

    print("Election Results")
    print("---------------------------------------")

    
    totalvotes = 0
    Khan = 0
    Li = 0
    Correy = 0
    O_Tooley = 0
    for row in csvreader:
        totalvotes += 1
        if row[2] == "Khan":
            Khan = Khan + 1
        elif row[2] == "Li":
            Li = Li + 1
        elif row[2] == "Correy":
            Correy == Correy + 1
        else:
            O_Tooley = O_Tooley + 1

    Khanpercentage = Khan /totalvotes * 100
    Lipercentage = Li /totalvotes * 100
    Correypercentage = Correy /totalvotes * 100
    O_Tooleypercentage = O_Tooley / totalvotes * 100
    
    
    print("Total Votes:" + " " + str(totalvotes))
    print("Khan:" + " " + str(Khanpercentage) + "%" + "  " + "(" + str(Khan) + ")")
    print("Li:" + " " + str(Lipercentage) + "%" + "  " + "(" + str(Li) + ")")
    print("Correy:" + " " + str(Correypercentage) + "%" + "  " + "(" + str(Correy) + ")")
    print("O'Tooley:" + " " + str(O_Tooleypercentage) + "%" + "  " + "(" + str(O_Tooley) + ")")
    
    print("---------------------------------------")
    
    Winner = []

    Winner.append(Khan)
    Winner.append(Li)
    Winner.append(Correy)
    Winner.append(O_Tooley)

    Findwinner = max(winner)

    print(Findwinner)



    #listcsvreader = list(csvreader)
    #print(listcsvreader)

        #list the different variables
        #Khan = 0
        #Li = 0
        #Correy = 0
        #O_Tooley = 0
        #loop through 3rdd column of file
        #for row[2] in csvreader:
            #if 
            
            #Khan = khan + 1
            

    

