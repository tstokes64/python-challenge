import csv
import sys
sys.stdout = open("Solutions_Pypoll.txt", "w")

with open('election_data.csv', newline= '') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    Candidate =[]

    for row in csv_reader:
        Candidate.append(str(row[2]))

    Total_Votes = len(Candidate)
    Khan_votes = Candidate.count("Khan")
    Correy_votes = Candidate.count("Correy")  
    Li_votes = Candidate.count("Li")
    OTooley_votes = Candidate.count("O'Tooley") 

    def most_frequent(Candidate): 
        return max(set(Candidate), key = Candidate.count) 
  
    print(most_frequent(Candidate)) 
    print("Election Results")
    print("-----------------------")
    print(f"Total Votes: {Total_Votes}")
    print("-----------------------")
    print(f"Khan: {(round((Khan_votes/Total_Votes),5)*100)}% ({Khan_votes})")
    print(f"Correy: {(round((Correy_votes/Total_Votes),5)*100)}% ({Correy_votes})")
    print(f"Li: {(round(((Li_votes/Total_Votes)*100),3))}% ({Li_votes})")
    print(f"O' Tooley: {(round((OTooley_votes/Total_Votes),5)*100)}% ({OTooley_votes})")
    print('-------------------')
    print(f'Winner: {(most_frequent(Candidate))}')
    print('-------------------')

    