# import python and OS add-on to open csv file
import csv
import os

# Used in 'for' loop to count the total months 
total_months = 0

# Used in 'for' loop to sum the profit/losses
total_profit = 0

# Used in 'for' loop to calculate average change
avg_change = 0

# Used in 'for' loop to calculate greatest profits
increase_profit = 0

# Used in 'for' loop to calculate least profits
decrease_profit = 0

# Open the csv file
with open('03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =',')

    # skip first row
    next(csv_file)

    csv_reader = list(csv_reader)
    previous_profit = int(csv_reader[0][1])
    # The 'for' loop calculate
    
    
    for row in csv_reader:
        
        current_profit = int(row[1])

        # Count each row to get the number of months; ignore first row
        total_months = total_months + 1

        # Sum the Profit/Losses column row by row
        total_profit = total_profit + current_profit

        # Average change
        current_change = current_profit - previous_profit
        previous_profit = current_profit
        avg_change = avg_change + current_change

        # Calculate Greatest Increase
        if current_change > increase_profit : 
            increase_profit = current_change 
            increase_month = row[0]

        if current_change < decrease_profit :
            decrease_profit = current_change
            decrease_month = row[0]
    
        
   
    # calculate final average change month to month  
    final_change = round(avg_change / (total_months - 1),2)   
    
    
    # Print("Financial Analysis", "----------------------------",sep="\n")  If I wanted to print in one function but decided against it   
    
    
    
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total : ${total_profit}")
print(f"Average Change: ${final_change}")
print(f"Greatest Increase in Profits: {increase_month} (${increase_profit})")
print(f"Greatest Decrease in Profits: {decrease_month} (${decrease_profit})")

# Write csv file
output_path = os.path.join("..", "analysis", "main.csv" )

with open(output_path, 'w', newline='') as writefile:

    csvwriter = csv.writer(writefile, delimiter=',')

    csvwriter.writerow("Financial Analysis")
    csvwriter.writerow("----------------------------")
    csvwriter.writerow(f"Total Months: {total_months}")
    csvwriter.writerow(f"Total : ${total_profit}")
    csvwriter.writerow(f"Average Change: ${final_change}")
    csvwriter.writerow(f"Greatest Increase in Profits: {increase_month} (${increase_profit})")
    csvwriter.writerow(f"Greatest Decrease in Profits: {decrease_month} (${decrease_profit})")