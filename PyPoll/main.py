# Import os and csv 
import os
import csv

# Variable for total votes
total_votes = 0

# Array of candidates
candidates =[]

csvfile = os.path.join('03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')

with open(csvfile, newline ='') as csv_file:
    csvreader = csv.reader(csv_file,delimiter = ',')
    
    next(csvreader)

    for row in csvreader:
        
        # Counting total votes
        total_votes = total_votes + 1

        condition = False
        
        # If candidate is already in candidates array then add 1 to their vote 
        for candidate in candidates:
            if candidate[1] == row[2]:
                candidate[0] = candidate[0] + 1
                condition = True
                break
        
            
        # Add new candidate 
        if condition == False:
            new_candidate = [1, row[2]]
            candidates.append(new_candidate)




candidates.sort(reverse=True)

print("")
print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")

for candidate in candidates:
    print(f'{candidate[1]}: {100*candidate[0]/total_votes:.3f}% ({candidate[0]})')
print("-------------------------")
print(f'Winner: {candidates[0][1]}')
print("-------------------------")



                
            

