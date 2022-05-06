# Import the datetime class from the datetime module.
import datetime as dt
import csv
import os
import random


file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        print(row)

    print(headers)
    
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")
    # Write three counties to the file.
    txt_file.write("Counties in election\n")
    txt_file.write("--------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
# Open the election results and read the file.
with open(file_to_load) as election_data:
     print(election_data)


# print(dir(os.path))
#
# for p in dir(os.path):
#     print(p)

# To do: perform analysis.

#  2 Write down the names of all the candidates.
#  3 Add a vote count for each candidate.
#  4 Get the total votes for each candidate.
#  5 Get the total votes cast for the election.

# The total number of votes cast
# the complete list of candidates received votes
# percentage of votes to each candidate
# total number of votes each candidate won
# the winner of the election based on popular vote

# Close the file.
election_data.close()
txt_file.close()


