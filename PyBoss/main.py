import os
# IMport dict for the state abbreviation
import state_abbr
import re
dob_formatted = []
new_table = []
filepath = os.path.join("employee_data.csv")

with open("output_employee_data.csv", "w+") as out_file:
    out_file.write("Emp ID,First Name,Last Name,DOB,SSN,State\n")
    with open (filepath, "r") as file:
        next(file)
        for line in file:
            row = line.strip().split(",")
            name = row[1]
            dob = row[2]
            ssn = row[3]
            ssn_list = ssn.split(" ")
            name_list = name.split(" ")
            #print(len(name_list))
            first_name = name_list[0]
            last_name = name_list[1]
        #print(first_name)
        #print(last_name)
        #print(row[2])
            dob_list = dob.split("-")
        #print(dob_list)
            dob_formatted_l = [dob_list[1], dob_list[2], dob_list[0]]
        #print(dob_formatted)
        
            dob_formattedcolumn = ("-").join(dob_formatted_l)
        #print(dob_formattedcolumn)
        
        #print(new_table)
        
        
        #for k,v in state_abbr.us_state_abbrev.items():
        ## Print count of each word in a list
         #   print (row[0], v)

            trans_state = row[4]
            if trans_state in state_abbr.us_state_abbrev:
                trans_state = state_abbr.us_state_abbrev[trans_state]

        # trans_ssn = '***-**-'+ssn[-4:]
            p=re.compile(r'.*(\d{4})')
            trans_ssn = '***-**-'+p.match(ssn)[1]
            #trans_ssn = p.match(ssn)[1]
        # print(trans_ssn)
            new_table = [row[0], first_name, last_name, dob_formattedcolumn,trans_ssn, trans_state]      
            #print(new_table)
            output_line = ",".join(new_table) + "\n"
            out_file.write(output_line)
        
    
