# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
        
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Initialize list to store csv data
    votes = []
    candidates = []
    count_votes = []
    unique_cand = []

    # Print header of the output
    print('Election Results')
    print('__________________________')
    print('')
    
    # Read each row of data after the header
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])
    
    # Calculate the total number of votes cast
    total_votes = len(votes)
    print('Total Votes: ', total_votes)
    print('__________________________')
    
    # Create a complete list of candidates who received votes
    list_candidates = (list(set(candidates)))

    # Calculate the percentage of votes each candidate won and the total number of votes each candidate won
    for i in list_candidates:
        print(i,': ','%.3f'%((candidates.count(i)/total_votes)*100),'% ','(',candidates.count(i),')')
        count_votes.append(candidates.count(i))
        unique_cand.append(i)
    print('__________________________')

    # Print the winner of the election based on popular vote
    winner_count = max(count_votes)
    print('Winner: ',unique_cand[count_votes.index(winner_count)])
    print('__________________________')

# Export a text file with the results
output_path = os.path.join( "Analysis", "Results.txt")    

with open(output_path, 'w') as file_text:    

    file_text.write('Election Results\n')
    file_text.write('__________________________\n')
    file_text.write('\n')
    file_text.write('Total Votes: '+ str(total_votes) +'\n')
    file_text.write('__________________________\n')
    for i in list_candidates:
        file_text.write(str(i)+': '+str('%.3f'%((candidates.count(i)/total_votes)*100))
                        +'% '+'('+ str(candidates.count(i))+')\n')

    file_text.write('__________________________\n')
    file_text.write('Winner: '+ str(unique_cand[count_votes.index(winner_count)])+'\n')
    file_text.write('__________________________')
 