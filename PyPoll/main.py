import os
import csv

csvpath = "Resources/election_data.csv"

#Open file and use the reader object to read it
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=(','))

#Use next() function to skip file's header
    next(csvreader)

#Print
    Header = "Election Results"
    print(Header)
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
    Khanpercentage = round((Khan /totalvotes * 100), 1)
    Lipercentage = round(Li /totalvotes * 100, 1)
    Correypercentage = round(Correy /totalvotes * 100, 1)
    O_Tooleypercentage = round(O_Tooley / totalvotes * 100, 1)
    
#Convert findings into string to concatenate with other strings when printing in Terminal 
    print("Total Votes:" + " " + str(totalvotes))
    print("Khan:" + " " + str(Khanpercentage) + "%" + "  " + "(" + str(Khan) + ")")
    print("Li:" + " " + str(Lipercentage) + "%" + "  " + "(" + str(Li) + ")")
    print("Correy:" + " " + str(Correypercentage) + "%" + "  " + "(" + str(Correy) + ")")
    print("O'Tooley:" + " " + str(O_Tooleypercentage) + "%" + "  " + "(" + str(O_Tooley) + ")")
    
    print("---------------------------------------")

#Create a dictionary to associate each candidate with the number of vote they gathered    
    Winner = {"Khan": 0, "Li": 0, "Correy": 0, "O'Tooley": 0}

    Winner["Khan"] = [Khan, Khanpercentage]
    Winner["Li"] = [Li, Lipercentage]
    Winner["Correy"] = [Correy, Correypercentage]
    Winner["O'Tooley"] = [O_Tooley, O_Tooleypercentage]

#Find winner by using max() function 
    Findwinner = max(Winner, key=Winner.get)

    print("Winner:" + " " + str(Findwinner))

outputfile = "Analysis/PyPoll"

#votes = totalvotes

pypoll = [Winner, Findwinner]

with open(outputfile, 'w') as datafile:
    csvwriter = csv.writer(datafile)

    csvwriter.writerow([Header])
    csvwriter.writerows(Winner)
