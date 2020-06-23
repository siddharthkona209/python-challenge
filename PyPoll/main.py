import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))

csvpath = os.path.join('Resources','election_data.csv')
csvmake = os.path.join('analysis','Voter_Turnout.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    Candidate = []
    Percents = []
    Votes = []
    Khan = 0
    Correy = 0
    Li = 0
    Tooley = 0
    Total = 0
    index = 0
    for row in csvreader:
        Total = Total + 1
        if (row[2] in Candidate):
            pass
        else:
            Candidate.append(row[2])
        if row[2] == "Khan":
            Khan = Khan + 1
        elif row[2] == "Correy":
            Correy = Correy + 1
        elif row[2] == "Li":
            Li = Li + 1
        else:
            Tooley = Tooley + 1
        
        
    StrTotal = ("Total Votes: " + str(Total))
    print(StrTotal)
    print(Candidate)
    Votes.append(Khan)
    Votes.append(Correy)
    Votes.append(Li)
    Votes.append(Tooley)
    Khan2 = Khan/Total * 100
    Correy2 = Correy/Total * 100
    Li2 = Li/Total * 100
    Tooley2 = Tooley/Total * 100
    Percents.append(str(round(Khan2))+"%")
    Percents.append(str(round(Correy2))+"%")
    Percents.append(str(round(Li2))+"%")
    Percents.append(str(round(Tooley2))+"%")
    print(Votes)
    print(Percents)

    Solution = zip(Candidate,Votes,Percents)

    index = Votes.index(max(Votes))
    #print(str(index))
    StrWinner = ("Winner: " + Candidate[index])
    print(StrWinner)
    
with open(csvmake,"w") as csvscript:
    csvwriter = csv.writer(csvscript, delimiter="|")

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["________________________________"])
    csvwriter.writerow([StrTotal])
    csvwriter.writerow(["________________________________"])
    csvwriter.writerows(Solution)
    csvwriter.writerow(["________________________________"])
    csvwriter.writerow([StrWinner])
    csvwriter.writerow(["________________________________"])





