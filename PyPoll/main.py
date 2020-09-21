#Import modules
import os

#Module for reading csv
import csv
csvpath=os.path.join('/Users/medinai/Desktop/python-challenge/PyPoll/Resources/election_data.csv')

#Variable for total votes
TotalVotes = 0

Candidates=[]
uniqueCandidates = []
VotesPerCandidate=[]
VotePercent=[]

#Reading using csv module
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    first_row=next(csvreader)

    TotalVotes = TotalVotes + 1

    #Read each row of data after the header
    for row in csvreader:
        #print(row) 
        #Total votes
        TotalVotes = TotalVotes + 1
        
        #List with candidate names - Candidates 
        Candidates.append(row[2])
    #Converting Candidates into a set with unique candidate names only
    for i in set(Candidates):
        uniqueCandidates.append(i)

        #Number of votes per unique candidate
        Votes = Candidates.count(i)
        VotesPerCandidate.append(Votes)
        
        #Percent of votes for unique candidate (formatted as percent with 3 decimals)
        Percent = "{:.3%}".format(Votes/TotalVotes)
        VotePercent.append(Percent)

#ziplists = zip(uniqueCandidates, VotesPerCandidate, VotePercent)

#VotesPerCandidate.sort() #Why sorts Candidates & % together but TotalVotes messed up?
#sorted_candidate=sorted(VotesPerCandidate, key=VotesPerCandidate.__getitem__)

# Set variable for output file
output_file = os.path.join("/Users/medinai/Desktop/python-challenge/PyPoll/analysis/output.csv")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    
    writer.writerow(["Election Results"])
    writer.writerow(['-'*35])
    writer.writerow([f'Total Votes: {TotalVotes}'])
    writer.writerow(['-'*35])
    for x in range(len(uniqueCandidates)):
        writer.writerow([f"{uniqueCandidates[x]} : {VotePercent[x]} ({VotesPerCandidate[x]})"])
    writer.writerow(['-'*35])




# print("Election Results")
# print("-"*30)
# print(f"Total Votes: {TotalVotes}")
# print("-"*30)
# print (ziplists)
#for x in range(len(uniqueCandidates)):
 #   print(f"{uniqueCandidates[x]} : {VotePercent[x]} ({VotesPerCandidate[x]})")
#print("-"*30)
#print(f"Winner: {sorted_candidate[-1]}")
#print(f"CSV Header: {csv_header}")
