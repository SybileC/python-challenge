import os
import csv

csvpath = "Resources/election_data.csv"

#Open file and use the reader object to read it
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=(','))

#Use next() function to skip file's header
    next(csvreader)

#Print Header
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
#Add each line to determine the number of votes
        totalvotes += 1
#Use If function to count votes for each candidate  
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

#Create a dictionary to associate each candidate with the number of votes they garnered    
    Winner = {"Khan": 0, "Li": 0, "Correy": 0, "O'Tooley": 0}

    Winner["Khan"] = [Khan]
    Winner["Li"] = [Li]
    Winner["Correy"] = [Correy]
    Winner["O'Tooley"] = [O_Tooley]

#Find winner by using max() function 
    Findwinner = max(Winner, key=Winner.get)

    print("Winner:" + " " + str(Findwinner))

#Create output path for csv file to be created
outputfile = "Analysis/PyPoll"

#Create 3 lists (candidates, number of votes for each candidate, and percentage of vote for each candidate) 
Candidates = ["Khan", "Li", "Correy", "O'Tooley"]
Candidatesvotes = [Khan, Li, Correy, O_Tooley]
Candidatespercentagevote = [Khanpercentage, Lipercentage, Correypercentage, O_Tooleypercentage]

#Use zip function to combine 3 lists
pypoll = zip(Candidates, Candidatesvotes, Candidatespercentagevote)

#Open output file and use the writer object to edit file
with open(outputfile, 'w') as datafile:
    csvwriter = csv.writer(datafile)

#Print in rows 
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["Total Votes", totalvotes])
    csvwriter.writerows(pypoll)
    csvwriter.writerow(["Winner", Findwinner])
    
