import os
import math
#Initializing the variables declared
winner = ''
winner_votes=0
total_votes = 0
unique_list = []
dict = {}
#Setitng the filepath for input file election_data.csv
filepath_input = os.path.join("Resources", "election_data.csv")
#Setitng the filepath for output file output_election_data.csv
filepath_output = os.path.join("Resources", "output_election_data.csv")


# Opening the file in write mode
with open(filepath_output, "w+") as out_file:
    # Opening the file in read mode
    with open (filepath_input, "r") as file:
        # Skipping the header to go to the next row
        next(file)
        for line in file:
            row = line.strip().split(",")
            voter_id = row[0]
            
            # Calculating the total number of votes 
            total_votes +=  1 

            county = row[1]
            candidates = row[2]
            candidates_list = candidates.split("\n")

            # Calculating the list of candidates who won votes
            if(candidates in dict):
                dict[candidates] = dict[candidates]+1
            else:
                dict[candidates] = 1
        
            if candidates_list not in unique_list: 
                unique_list.append(candidates_list)
            unique_element = unique_list[0]    

    # Calculating the winner among the candidates who won votes
    for key in dict:
        if(dict[key] > winner_votes):
            winner=key
            winner_votes = dict[key]


#____________Print output
    output1= "Election Results"
    output2 = "-----------------------"
    output3= "Total Votes: " + str(total_votes)
    print(output1)
    print(output2)
    print(output3)
    print(output2)

    for key in dict:
        pct = round(dict[key]/total_votes*100,4)
        output4 = key +' : '+str("{0:.3f}".format(pct))+'% ('+str(dict[key])+ ')'
        print (output4)
    output5 = 'Winner: '+winner
    print(output2)
    print (output5)
    print(output2)

    # Wring the analysis result in output file output_election_data.csv
    out_file.write(output1 + "\n")
    out_file.write(output2 + "\n") 
    out_file.write(output3 + "\n")
    out_file.write(output2 + "\n")

    for key in dict:
        pct = round(dict[key]/total_votes*100,4)
        output4 = key +': '+str("{0:.3f}".format(pct))+'% ('+str(dict[key])+ ')'
        out_file.write(output4 + "\n")

    out_file.write(output2 + "\n")
    out_file.write(output5 + "\n")
    out_file.write(output2 + "\n")

