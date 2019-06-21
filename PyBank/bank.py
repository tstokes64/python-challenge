
import csv
import os

with open('budget_data.csv', newline= '') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #csv_header = next(csv_reader)
    next(csv_reader)
    #Counts total rows in CSV file.
    months = []
    profits_losses = []
    monthly_net = []
    for row in csv_reader:
        months.append(str(row[0]))
        profits_losses.append(int(row[1]))
    Change = []
    for i in range(len(profits_losses)-1):
        change = profits_losses[i+1] - profits_losses[i]
        monthly_net.append(change)
        avgChange = (sum(monthly_net))/(len(monthly_net)) 
    total = sum(profits_losses)
    total_months = len(months)
    print('Financial Statement')
    print('-------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: {total}')
    print(f'Average Change:{avgChange}')
    print(f'Greatest Increase in Profits:{max(monthly_net)}')
    print(f'Greatest Decrease in Profits:{min(monthly_net)}')


