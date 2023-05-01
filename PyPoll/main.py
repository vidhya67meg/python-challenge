import os
# Module for reading CSV files
import csv
csvpath = os.path.join('Resources','election_data.csv')
    
# Declare variables
total_votes = 0
candidate_votes = {}
max_vote = 0
max_vote_name = str

# CSV reader specifies delimiter and variable that holds contents
with open (csvpath) as csvfile :
    csvreader = csv.reader(csvfile, delimiter = ',')
    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header   
    for row in csvreader:
        total_votes = total_votes + 1
        # assigning votes to unique candidates
        candidate_votes[row[2]] = candidate_votes.get(row[2], 0) + 1
    
        

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
# Printing the unique candidates determined, with their respective votes and percentage of votes
for candidate in candidate_votes:
    vote = candidate_votes[candidate]
    print(f"{candidate}: {round((vote/total_votes)*100,3)}% ({vote})")
    # Determining winner by declaring variables and finding maximum value in unique candidate list
    if  vote > max_vote:
        max_vote = vote
        max_vote_name = candidate
print("-------------------------")
print(f"Winner: {max_vote_name}")
print("-------------------------")
  
# Specify the file to write to
txtpath = os.path.join('analysis','results.txt')
# Open the file using "write" mode. 
with open(txtpath, 'w') as f:
    # Write the results
    f.write("Election Results\n")
    f.write("----------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("----------------------------\n")
    for candidate in candidate_votes:
        vote = candidate_votes[candidate]
        f.write(f"{candidate}: {round((vote/total_votes)*100,3)}% ({vote})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {max_vote_name}\n")
    f.write("-------------------------\n")

    



