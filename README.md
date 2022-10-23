# Election Analysis

## Overview of Election Audit
The purpose of this analysis was to create a voter counter to collect total votes from different districts. The goal was to find the total number of votes cast and to calculate the number of votes each candidate received. 

## Election-Audit Result 
  -How many votes were cast in this congressional election?
  -Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  -Which county had the largest number of votes?
  -Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  -Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

### Breakdown
The analysis based on the data collected shows:
  -There were 369,711 total votes cast

There were three counties in this analysis
  -Jefferson (38855 Votes) or (10.5%)
  -Denver (306055 Votes) or (82.8%)
  -Arapahoe (24801 Votes) or (6.7%)

Denver county had the most votes with 306,055

There were three candidates
  -Charles Casper Stockham: 23.0% (85,213)
  -Diana DeGette: 73.8% (272,892)
  -Raymon Anthony Doane: 3.1% (11,606)

Diana DeGette won the election with 73.8% of the votes  (272,892 votes)


![Capture](https://user-images.githubusercontent.com/112728628/197407256-101faa38-5880-4e4d-9fc4-b758b418a6f1.PNG)


## Election-Audit Summary 
This script can be used in any election with a few simple modifications to the code. The script can:
  -find counties
  -find the largest turnout counties
  -find candidate's names
  -calculate the percentage of votes per candidate
  -can determine who the winner is 

Modifying the load command is the only thing that would need to be changed in order for it to pull data from a county or state you wish to see.    
`file_to_load = os.path.join("Resources","election_results.csv")` 
`file_to_save = os.path.join("Analysis", "election_analysis.txt")`
