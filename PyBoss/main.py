import os
# Import dict for the state abbreviation
import state_abbr
import re

# Declaring and initializing the variables
dob_formatted = []
new_table = []

# Setting the filepath for input file (employee_data.csv)
filepath1 = os.path.join("employee_data.csv")

# Setting the filepath for output file (output_employee_data.csv)
filepath2 = os.path.join("output_employee_data.csv")

with open(filepath2, "w+") as out_file:
    header = ("Emp ID,First Name,Last Name,DOB,SSN,State\n")
    out_file.write(header)
    with open (filepath1, "r") as file:
        # Skipping the header and move to the fist row
        next(file)
        for line in file:
            # Splitting each row elements by comma (,)
            row = line.strip().split(",")
            name = row[1]
            dob = row[2]
            ssn = row[3]

            # Splitting the Name column into two columns (First Name and Last Name)
            name_list = name.split(" ")
            first_name = name_list[0]
            last_name = name_list[1]
            
            #Changing the date to `MM/DD/YYYY` format
            dob_list = dob.split("-")
            dob_formatted_l = [dob_list[1], dob_list[2], dob_list[0]]
            dob_formattedcolumn = ("-").join(dob_formatted_l)
            
            ssn_list = ssn.split(" ")        
        
            # Changing the state names to two letter abbreviations 
            # checking if transformed state(trans_state) in dictionary us_state_abbrev then converting it into its abbreviated form
            trans_state = row[4]
            if trans_state in state_abbr.us_state_abbrev:
                trans_state = state_abbr.us_state_abbrev[trans_state]

            # Using re module to transform SSN in the format '***-**-dddd
            p=re.compile(r'.*(\d{4})')
            trans_ssn = '***-**-'+p.match(ssn)[1]
            
            # New table with employee records in the required format
            new_table = [row[0], first_name, last_name, dob_formattedcolumn,trans_ssn, trans_state]      
            output_line = ",".join(new_table) + "\n"
        
            # Print(new_table)
            print(output_line)
            
            # Write into the output file
            out_file.write(output_line)
        
    
