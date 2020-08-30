import os
import csv

csvpath = "Resources/election_data.csv"

#open file and convert it into a 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=(','))

#Use next() function to skip file's header
    next(csvreader)

#Print 
    print("Election Results")
    print("---------------------------------------")

#define the total number of votes and the total number for each candidate as variables with zero value     
    totalvotes = 0
    Khan = 0
    Li = 0
    Correy = 0
    O_Tooley = 0

#Use for loop to go through each row and add values to each variable    
    for row in csvreader:
#Add the value of each row from first column to get totalvotes
        totalvotes += 1
#Use If function to count for votes for each candidate  
        if row[2] == "Khan":
            Khan = Khan + 1
        elif row[2] == "Li":
            Li = Li + 1
        elif row[2] == "Correy":
            Correy = Correy + 1
        else:
            O_Tooley = O_Tooley + 1

#Calculate the percentage of votes for each candidate based on the total number of votes
    Khanpercentage = Khan /totalvotes * 100
    Lipercentage = Li /totalvotes * 100
    Correypercentage = Correy /totalvotes * 100
    O_Tooleypercentage = O_Tooley / totalvotes * 100
    
#Convert findings into string to concatenate with other strings when printing in Terminal 
    print("Total Votes:" + " " + str(totalvotes))
    print("Khan:" + " " + str(Khanpercentage) + "%" + "  " + "(" + str(Khan) + ")")
    print("Li:" + " " + str(Lipercentage) + "%" + "  " + "(" + str(Li) + ")")
    print("Correy:" + " " + str(Correypercentage) + "%" + "  " + "(" + str(Correy) + ")")
    print("O'Tooley:" + " " + str(O_Tooleypercentage) + "%" + "  " + "(" + str(O_Tooley) + ")")
    
    print("---------------------------------------")

#Create a dictionary to associate each candidate with the number of vote they gathered    
    Winner = {"Khan": 0, "Li": 0, "Correy": 0, "O'Tooley": 0}

    Winner["Khan"] = Khan
    Winner["Li"] = Li
    Winner["Correy"] = Correy
    Winner["O'Tooley"] = O_Tooley

#
    Findwinner = max(Winner, key=Winner.get)

    print("Winner:" + " " + str(Findwinner))

outputfile = "Analysis/PyPoll"

with open(outputfile, 'w') as datafile:
    csvwriter = csv.writer(datafile)

    csvwriter.writerow("Election Results")
    csvwriter.writerow("---------------------------------------")
    csvwriter.writerow("Total Votes:" + " " + str(totalvotes))
    csvwriter.writerow("Khan:" + " " + str(Khanpercentage) + "%" + "  " + "(" + str(Khan) + ")")
    csvwriter.writerow("Li:" + " " + str(Lipercentage) + "%" + "  " + "(" + str(Li) + ")")
    csvwriter.writerow("Correy:" + " " + str(Correypercentage) + "%" + "  " + "(" + str(Correy) + ")")
    csvwriter.writerow("O'Tooley:" + " " + str(O_Tooleypercentage) + "%" + "  " + "(" + str(O_Tooley) + ")")
    csvwriter.writerow("---------------------------------------")
    csvwriter.writerow("Winner:" + " " + str(Findwinner))
