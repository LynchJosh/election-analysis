print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
my_tuple = ()
counties_tuple = ("Arapahoe","Denver","Jefferson")
counties = {}
counties_dict = {}
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
voting_data = []
voting_data.append({"county": "El Paso", "registered_voters":461149})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")

candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("what was the total number of votes in the election?"))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)


for county in counties:
    print(county)

for i in range (len(counties)):
    print(counties[i])


for county in counties_dict:
    print(county)


for voters in counties_dict.values():
    print(voters)

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)




