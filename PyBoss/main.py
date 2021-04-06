# Import needed modules
import os
import csv

# Updated dictionary variable defined
final_list = [['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']]


# READ-FILE
# Open read-only csv file
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

        # Append updated DOB to our list
        individual_list.append(month_day_year)


        # SOCIAL SECURITY NUMBER
        # Splitting up social security number to focus on the last four digits
        ssn = row[3].split('-')

        # Create new SSN and append to our list
        new_ssn = f'***-**-{ssn[2]}'
        individual_list.append(new_ssn)


        # STATE
        # Define state abbreviations dictionary (link provided in the README file)

        us_state_abbrev = {
            'Alabama': 'AL',
            'Alaska': 'AK',
            'Arizona': 'AZ',
            'Arkansas': 'AR',
            'California': 'CA',
            'Colorado': 'CO',
            'Connecticut': 'CT',
            'Delaware': 'DE',
            'Florida': 'FL',
            'Georgia': 'GA',
            'Hawaii': 'HI',
            'Idaho': 'ID',
            'Illinois': 'IL',
            'Indiana': 'IN',
            'Iowa': 'IA',
            'Kansas': 'KS',
            'Kentucky': 'KY',
            'Louisiana': 'LA',
            'Maine': 'ME',
            'Maryland': 'MD',
            'Massachusetts': 'MA',
            'Michigan': 'MI',
            'Minnesota': 'MN',
            'Mississippi': 'MS',
            'Missouri': 'MO',
            'Montana': 'MT',
            'Nebraska': 'NE',
            'Nevada': 'NV',
            'New Hampshire': 'NH',
            'New Jersey': 'NJ',
            'New Mexico': 'NM',
            'New York': 'NY',
            'North Carolina': 'NC',
            'North Dakota': 'ND',
            'Ohio': 'OH',
            'Oklahoma': 'OK',
            'Oregon': 'OR',
            'Pennsylvania': 'PA',
            'Rhode Island': 'RI',
            'South Carolina': 'SC',
            'South Dakota': 'SD',
            'Tennessee': 'TN',
            'Texas': 'TX',
            'Utah': 'UT',
            'Vermont': 'VT',
            'Virginia': 'VA',
            'Washington': 'WA',
            'West Virginia': 'WV',
            'Wisconsin': 'WI',
            'Wyoming': 'WY',
        }        

        # Using state name as key, find state abbreviation
        state_abbrev = us_state_abbrev[row[4]]
        
        # Add state abbreviation to our list
        individual_list.append(state_abbrev)
        
        
        # ALL VALUES HAVE BEEN CALCULATED
        # Append our list to the final list
        final_list.append(individual_list)


# WRITE-FILE
# Open write-only csv file

csvpath = os.path.join('Analysis','employee_revised_data.csv')

with open(csvpath,'w',newline = '') as csvfile:

    csvwriter = csv.writer(csvfile,delimiter = ',') 
    
    # WRITE TO FILE
    # Iterate through each record and add to the csv file    
    for record in final_list:
            csvwriter.writerow(record)


