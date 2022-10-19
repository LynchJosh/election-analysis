# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
    #Read and print the header
    #headers = next(file_reader)
    #print(headers)





#file_to_save = os.path.join("analysis","election_analysis.txt")
#with open(file_to_save, "w") as txt_file:
 #txt_file.write("Countries in the Election\n")  
#txt_file.write("-------------------------\n")  
#txt_file.write("Arapahoe\nDenver\nJefferson")




