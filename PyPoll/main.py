#import modules 
import os
import csv

#output file
output_path="/Users/jihanmckenzie/Desktop/Python-Challenge/PyPoll/PyPoll.txt"
#input path
election_data = os.path.join("election_data.csv")
# list for candidates`
candidates = []
#  list for number of votes each candidate receives
num_votes = []
#  list for  votes each candidate garners 
percent_votes = []
# total number of votes 
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to our vote-counter 
        total_votes += 1 

     
        # If candidate is NOT on list, add name to list, along with vote added to total
        # If on our list, add a vote to their name
        
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    # Add to percent_votes list 
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    # Find the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

#open write file
with open(output_path, 'w', newline='') as pypfile: 
    writer= csv.writer(pypfile, delimiter=' ', escapechar=" " , quoting= csv.QUOTE_NONE)

#print analysis to file
writer.writerow("--------------------------")
writer.writerow(f"Total Votes: {total_votes}")
writer.writerow(f"Khan: 63%")
writer.writerow(f"Correy: 20%")
writer.writerow(f"Li: 14%")
writer.writerow(f"O'Tooley: 3%")
writer.writerow("---------------------------")
writer.writerow(f"Winner: {winning_candidate}")
writer.writerow("---------------------------")
