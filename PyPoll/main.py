import os
import csv
import collections
from collections import Counter

# Path to collect data from the Resources folder
election_data_csv = os.path.join("Resources", "02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

# Define PyPoll's lists and variables
candidates = []
votes_per_candidate = {}
total_votes = 0
win_count = 0 
win_candidate = ""

# Open and read csv
with open(election_data_csv, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    #print(f"Header: {csv_header}") for Voter ID, Country and Candidate
    #Loop through each row of data after the header
    for row in csv_reader:

        if row[2] not in candidates:

            candidates.append(row[2]) 
            votes_per_candidate[row[2]] = 0 
        
        votes_per_candidate[row[2]] = votes_per_candidate[row[2]] + 1
        total_votes = total_votes + 1
    # Sort the list by ascending order
    sorted_list = sorted(votes_per_candidate.items())

    #Count votes per condidate and append to list.
   # count_candidate = counter (arrange_list)
#print(candidates)
#print(votes_per_candidate)
#print(sorted_list)
#print(total_votes)

#set file name
output_path = 'output.txt'
()
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("------------------\n")
    

    for candidate in candidates:
        votes = votes_per_candidate.get(candidate)
        votes_percentage = float(votes) / float(total_votes) * 100

        if votes > win_count:
            win_count = votes
            win_candidate = candidate
        file.write(f"{candidate}: {votes_percentage:.3f}% ({votes})\n")
        #print(f"Candidate: {candidate}\t Votes: {votes_percentage:.3f}% ({votes}) \n")
    file.write("------------------\n")
    file.write(f"Winner: {win_candidate}\n")
    file.write("------------------\n")
    #print(f"Winner: {win_candidate}")
print("Wrote to output.txt")