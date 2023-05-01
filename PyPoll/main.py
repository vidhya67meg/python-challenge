import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

# def vote_percentage (voting_data):
#     ballot_id = voting_data[0]
#     county = voting_data[1]
#     candidate = voting_data[2]

    

total_votes = 0
candidate_votes = {}
with open (csvpath) as csvfile :
    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvreader)

    
    for row in csvreader:
    
        total_votes = total_votes + 1
        candidate_votes[row[2]] = candidate_votes.get(row[2], 0) + 1
    
        
max_vote = 0
max_vote_name = str
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidate_votes:
    print(f"{candidate}: {round((candidate_votes[candidate]/total_votes)*100,3)}% ({candidate_votes[candidate]})")
    if candidate_votes[candidate] > max_vote:
        max_vote = candidate_votes[candidate]
        max_vote_name = candidate
print("-------------------------")
print(f"Winner: {max_vote_name}")
print("-------------------------")
  

txtpath = os.path.join('analysis','results.txt')

with open(txtpath, 'w') as f:
    f.write("Election Results\n")
    f.write("----------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("----------------------------\n")
    for candidate in candidate_votes:
         f.write(f"{candidate}: {round((candidate_votes[candidate]/total_votes)*100,3)}% ({candidate_votes[candidate]})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {max_vote_name}\n")
    f.write("-------------------------\n")

    



