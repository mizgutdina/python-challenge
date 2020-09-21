# Importing os module allows to create a file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('/Users/medinai/Desktop/python-challenge/PyBank/Resources/budget_data.csv')

#Denote arrays where all months & totals will be stored 
total_months = 0 
net_total_amount = 0

# Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #empty lists to store date, profit/loss and all changes
    date=[]
    profit_loss = []
    change = [] 
    average_change = []
    
    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        #Calculate total months
        total_months = total_months + 1
        
        #Calculate the net total amount
        net_total_amount = net_total_amount+int(row[1])

        #Point to respective data arrays
        date.append(row[0])
        profit_loss.append(row[1])
    #Calculate delta - difference between subsequent profit/losses
    for i in range(len(date)-1):
       change.append(int(profit_loss[i+1])-int(profit_loss[i]))
    
    #Find average change - sum of all changes of profit/loss over the number of changes
    average_change = str(round((sum(change)/len(change)),2))

    #Find largest value in the change array - greatest increase
    greatest_increase = max(change)
    
    #Find index of the greatest increase - the date it occured
    x = change.index(greatest_increase)
    date_increase = date[x+1]

    #Find smallest value - greatest decrease
    greatest_decrease = min(change)
    
    #Find date 
    y = change.index(greatest_decrease)
    date_decrease = (date[y+1])

#start of writing csv output file
#Set variable for output file
output_file = os.path.join("/Users/medinai/Desktop/python-challenge/PyBank/analysis/output.csv")

#Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-"*30])
    writer.writerow([f"Total Months: {total_months}"])
    writer.writerow([f"Total: ${net_total_amount}"])
    writer.writerow([f"Average Change: ${average_change}"])
    writer.writerow([f"Greatest Increase in Profits: {date_increase} $({greatest_increase})"])
    writer.writerow([f"Greatest Decrease in Profits: {date_decrease} $({greatest_decrease})"])

#end of writing csv output file

print("Financial Analysis")
print("-"*30)
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {date_increase} $({greatest_increase})")
print(f"Greatest Decrease in Profits: {date_decrease} $({greatest_decrease})")
    
    
