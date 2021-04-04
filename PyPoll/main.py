# Import os and csv 
import os
import csv

# Variable for total votes
total_votes = 0

# Create blank array of candidates. 'candidates' will be a list of candidates and their total votes. The first index of each unique candidate is the number of votes they earned. The second index is the candidate name. The reason for this is to making sorting the winner by the most votes easier later in the code. 
candidates =[]

# Open csv file process
csvfile = os.path.join('03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')

with open(csvfile, 'r', newline ='') as csv_file:
    csvreader = csv.reader(csv_file,delimiter = ',')
    
    # Store column headers
    headers = []
    for row in csvreader:
        num_of_cols = len(row)
        for x in range(0,num_of_cols):
            headers.append(row[x])
        break           

    # 'for' loop to calculate required outputs
    for row in csvreader:
        
        # Counting total votes
        total_votes = total_votes + 1
       
        # If candidate is already in candidates array then add 1 to their vote 
        condition = False
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

csvpath = os.path.join('analysis','main.csv')

with open(csvpath,'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f'Total Votes: {total_votes}'])
    csvwriter.writerow(["-------------------------"])

    for candidate in candidates:
        csvwriter.writerow([f'{candidate[1]}: {100*candidate[0]/total_votes:.3f}% ({candidate[0]})'])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f'Winner: {candidates[0][1]}'])
    csvwriter.writerow(["-------------------------"])


        





                
            

