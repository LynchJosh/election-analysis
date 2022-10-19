# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0 
candidate_options = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Read and print the header
    headers = next(file_reader)
    print(headers)

    #Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1 

        candidate_name = row[2]

        candidate_options.append(candidate_name)
# 3. Print the total votes.
#print(total_votes)
print(candidate_options)



#file_to_save = os.path.join("analysis","election_analysis.txt")
#with open(file_to_save, "w") as txt_file:
 #txt_file.write("Countries in the Election\n")  
#txt_file.write("-------------------------\n")  
#txt_file.write("Arapahoe\nDenver\nJefferson")




