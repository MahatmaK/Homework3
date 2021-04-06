# Import needed modules
import os
import csv


# Updated dictionary variable defined
final_list = [['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']]

# Open csv file
csvpath = os.path.join('Resources','03-Python_Homework_ExtraContent_Instructions_PyBoss_employee_data.csv')

with open(csvpath,'r', newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    next(csvreader)
    
    for row in csvreader:
        # Define new list we will work with
        individual_list = []
        

        # EMPLOYEE ID
        # Emp ID remains the same and is appended to the list
        individual_list.append(row[0])
        

        # FIRST AND LAST NAME
        # Searching for ' ' in Name column and splitting into two values
        split_name = row[1].split(' ')

        # Place first and last name into our list
        individual_list.append(split_name[0])
        individual_list.append(split_name[1])


        # DATE OF BIRTH
        # Splitting up the given date into year, month, and date
        year_month_day = row[2].split('-')

        # Recombine year_month_day into month_day_year with '/'
        month_day_year = f'{year_month_day[1]}/{year_month_day[2]}/{year_month_day[0]}'

        # Append updated DOB to list
        individual_list.append(month_day_year)

        


        
        

        break
    print(individual_list)
        

