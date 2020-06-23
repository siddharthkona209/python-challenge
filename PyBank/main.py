import os 
import csv 

os.chdir(os.path.dirname(os.path.abspath(__file__)))

csvpath = os.path.join('Resources','budget_data.csv')
csvmake = os.path.join('analysis','Financial_Analysis.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csvheader= next(csvreader)

    month = 0
    Total = 0
    Average = 0
    Greatest = 0
    Lowest = 0
    index = str()
    index2 = str()
    for row in csvreader:
        #print(row)
        month = month + 1
        Total = Total + int(row[1])
        if (int(row[1]) > Greatest):
            Greatest = int(row[1])
            index = row[0] + ", $" + str(row[1])
        elif (int(row[1]) < Lowest):
            Lowest = int(row[1])
            index2 = row[0] + ", $" + str(row[1])
    Average = round(Total/month,2)
    String1 = ("Total number of months: " + str(month))
    String2 = ("Total Profit/Losses: $" + str(Total))
    String3 = ("Average Profit/Losses: $" + str(Average))
    String4 = ("Greatest Increase: " + index)
    String5 = ("Greatest Decrease: " + index2)
    print(String1)
    print(String2)
    print(String3)
    print(String4)
    print(String5)

with open(csvmake,"w") as csvscript:
    csvwriter = csv.writer(csvscript)

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["____________________________"])
    csvwriter.writerow([String1])
    csvwriter.writerow([String2])
    csvwriter.writerow([String3])
    csvwriter.writerow([String4])
    csvwriter.writerow([String5])