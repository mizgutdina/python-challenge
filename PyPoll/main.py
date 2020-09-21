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
winners=[]

#Reading using csv module
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    #Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

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

ziplists = list(zip(uniqueCandidates, VotesPerCandidate, VotePercent))

for z in ziplists:
    if max(VotePercent) == z[2]:
        winners.append(z[0])

winner = winners[0]

#ziplists.sort()
#print(ziplists)
#VotesPerCandidate.sort() #Why sorts Candidates & % together but TotalVotes messed up?
#print(VotesPerCandidate.sort())

#start of writing csv
#Set variable for output file
output_file = os.path.join("/Users/medinai/Desktop/python-challenge/PyPoll/analysis/output.csv")

#Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    
    writer.writerow(["Election Results"])
    writer.writerow(['-'*35])
    writer.writerow([f'Total Votes: {TotalVotes}'])
    writer.writerow(['-'*35])
    for x in range(len(uniqueCandidates)):
        writer.writerow([f"{uniqueCandidates[x]} : {VotePercent[x]} ({VotesPerCandidate[x]})"])
    writer.writerow(['-'*35])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(['-'*35])
#end of writing csv

print("Election Results")
print("-"*30)
print(f"Total Votes: {TotalVotes}")
print("-"*30)
for x in range(len(uniqueCandidates)):
   print(f"{uniqueCandidates[x]} : {VotePercent[x]} ({VotesPerCandidate[x]})")
print("-"*30)
print(f"Winner: {winner}")
print("-"*30)

