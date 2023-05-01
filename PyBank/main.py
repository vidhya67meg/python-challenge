import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row  
    csv_header = next(csvreader)


    count = 0
    total_amount = 0
    change = 0
    previous_value = 0
    overall_change = 0
    greatest_increase = 0
    greatest_month = str
    greatest_decrease = 0
    greatest_decrease_month = str

    for row in csvreader:
       profit_loss = int(row[1])
       if count == 0:
           previous_value = profit_loss
       # total number of months
       count = count + 1
       # total amount of "profit/losses"
       total_amount = total_amount + profit_loss
       change = profit_loss - previous_value
       overall_change = overall_change + change
       previous_value = profit_loss
       if change > greatest_increase:
           greatest_increase = change
           greatest_month = row[0]
       if change < greatest_decrease:
           greatest_decrease = change
           greatest_decrease_month = row[0]



    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {count}")
    print(f"Total: ${total_amount}")
    print(f"Average Change: ${overall_change/(count-1)}")
    print(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

   
    

