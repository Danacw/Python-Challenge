import os
import csv

# Path to collect data from the Resources folder
pybank_csv = os.path.join("Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

#Create lists to store data
months = []
profit = []

#set up all variables. 
net_months = 1
max_increase_month = 1
max_decrease_month = 1
profit_change = 0
net_profit_change = 0
max_increase = 0
max_decrease = 0

# Read in the CSV file
with open(pybank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Asign csv header
    csv_header = next(csvreader)
    #Loop through the data (with for loop). Use append to add months and profits to list.
    for row in csvreader:
        #Months
        months.append(row[0])
        #print(len(months))
        #Profit
        profit.append(int(row[1]))
        #print(len(profit))
        
        
#Use while loop to continuously calculate profit each month. 
while net_months < len(profit):
    #Subtract profits from current month to previous month to get month-to-month change.
    profit_change = (profit[net_months] - profit[net_months - 1])
    #add all changes from one month to the next to find net change in profit. 
    net_profit_change += profit_change

    #if increase is greatest then 
    if profit_change > max_increase:
        max_increase =profit_change
        max_increase_month = net_months
    elif profit_change < max_decrease:
        max_decrease = profit_change
        max_decrease_month = net_months

    #continue counting the list month to month.
    net_months +=1 

#Set the file name and automate calculations.
output_path = 'output.txt'
()
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------\n")
    file.write(f"Total Months: {net_months}\n")
    file.write(f"Total: ${int(sum(profit))}\n")
    file.write(f"Average Change: ${round(net_profit_change/(net_months - 1),2)}\n")
    file.write(f"Greatest Increase in Profits: {months[max_increase_month]} (${round(max_increase)})\n")
    file.write(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${round(max_decrease)})\n")







    



