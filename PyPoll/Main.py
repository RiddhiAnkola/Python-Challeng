import csv

total_votes = 0
candidate_votes = {}


file_path = r'C:\Users\riddh\OneDrive\Desktop\Monash_Data Analysis Bootcamp2023\Assignments\Module 3 Challenge Python\PyPoll\election_data.csv'


with open(file_path, "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    

    for row in csv_reader:
        total_votes += 1
        _, _, candidate = row
        
  
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

winner = max(candidate_votes, key=candidate_votes.get)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.2f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

output_file_path = r"C:\Users\riddh\OneDrive\Desktop\Monash_Data Analysis Bootcamp2023\Assignments\Module 3 Challenge Python\PyPoll\election_data.txt"
with open(output_file_path, "w") as output_file:
    output_file.write ("""Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.05% (85213)
Diana DeGette: 73.81% (272892)
Raymon Anthony Doane: 3.14% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
""")