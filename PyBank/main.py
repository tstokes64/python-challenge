import csv
import os

with open('budget_data.csv', newline= '') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
   
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
   
    max_monthly = max(monthly_net)
    min_monthly = min(monthly_net)
    

    date_max = months[monthly_net.index(max_monthly)+1]
    date_min = months[monthly_net.index(min_monthly)+1]
    

    print('Financial Statement')
    print('-------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: {total}')
    print(f'Average Change:{avgChange}')
    print(f'Greatest Increase in Profits:{date_max} {max_monthly}')
    print(f'Greatest Decrease in Profits:{date_min} {min_monthly}')