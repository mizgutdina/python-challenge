# Importing os module allows to create a file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('/Users/medinai/Desktop/python-challenge/PyBank/Resources/budget_data.csv')

#Denote array where all months will be stored
TotalMonths = 0

# Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    first_row=next(csvreader)
    
    TotalMonths = TotalMonths + 1
   
    #empty list to store all changes
    change=[] 
    
    #net change
    profit_loss=[] 
    months=[]
    
    date=[]
    
    # Read each row of data after the header
    for row in csvreader:
     #   print(row)
        TotalMonths = TotalMonths + 1

# net_total_amount=0    
# with open(csvpath) as csvfile:
# # CSV reader specifies delimiter and variable that holds contents - csvfile
#     csvreader = csv.reader(csvfile, delimiter=',')

#     print(csvreader)

#     # Read the header row first (skip this step if there is now header)
#     csv_header = next(csvreader)
#     #print(f"CSV Header: {csv_header}")
    
#     first_row=next(csvreader)
    
#     #Define the function and have it accept the 'budget_data' as its sole parameter
#     for row in csvreader:
#         #Assign values to variables 
#         net_total_amount = net_total_amount + 1

#         #Net total anount
# net_total_amount = sum(profit_loss)



    #for i in range(len(date)-1):
     #   change.append(profit_loss[i+1]-profit_loss[i])
   

print("Financial Analysis")
print("-"*35)
print(f"Total Months: {TotalMonths}")
#print(f"Total: {net_total_amount}")
    #print (change)
    
