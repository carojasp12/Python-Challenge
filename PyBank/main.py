# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
        
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Print header of the output
    print('')
    print("Financial Analysis")
    print('________________________________________')
    print('')

    # Initialize list to store csv data 
    date = []
    profit = []
    changes = []

    # Read each row of data after the header
    for row in csvreader:
       date.append(row[0])
       profit.append(int(row[1]))
       
    # Count the total number of months included in the dataset
    total_moths = len(date) 
    print('Total Months:', total_moths) 

    # Calculate the net total amount of "Profit/Losses" over the entire period
    change_profit = sum(profit)
    print('Total: $',change_profit)

    # Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
    for i in range(1, total_moths):
        difference = (int(profit[i])) - (int(profit[i-1]))
        changes.append(difference)
    
    average_changes = sum(changes)/len(changes)
    print('Average Change: $','%.2f'% average_changes)
 
    # Calculate the greatest increase and decrease in profits (date and amount) over the entire period
    greatest_increase = max(changes)
    greatest_decrease = min(changes)
    increase_date = date[changes.index(greatest_increase)+1]
    decrease_date = date[changes.index(greatest_decrease)+1]

    print('Greatest Increase in Profits:',increase_date, '($',greatest_increase,')')
    print('Greatest Decrease in Profits:',decrease_date, '($',greatest_decrease,')')

# Export a text file with the results
output_path = os.path.join( "Analysis", "Results.txt")    

with open(output_path, 'w') as file_text:
    file_text.write('Financial Analysis'+'\n')
    file_text.write('________________________________________'+'\n')
    file_text.write(''+'\n')
    file_text.write('Total Months: ' + str(total_moths)+'\n')    
    file_text.write('Total: $'+ str(change_profit)+'\n')
    file_text.write('Average Change: $'+ str('%.2f'% average_changes)+'\n')
    file_text.write('Greatest Increase in Profits: '+ str(increase_date) + ' ($' + str(greatest_increase) +')'+'\n')
    file_text.write('Greatest Decrease in Profits: '+ str(decrease_date) + ' ($'+ str(greatest_decrease) +')'+'\n')