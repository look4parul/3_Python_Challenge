import os
#Initializing the variables declared
count = 0
totalPL= 0 
prevPL = 0
diffTotal =0
maxInc = 0
maxIncMonth = 'NULL'
maxDec = 0
maxDecMonth = 'NULL'

#Setitng the filepath for input file budget_data.csv
filepath = os.path.join("Resources", "budget_data.csv")
#Setitng the filepath for output file output_budget_file.csv
filepath_output = os.path.join("Resources", "output_budget_file.csv")

#Opening the file in write mode
with open(filepath_output, "w+") as out_file:

#Opening the file in read mode
    with open (filepath, "r") as file:
        #Skip the header and move to next row
        next(file)
        for line in file:
            row = line.strip().split(",")
            date = row[0]
        #Split the months and year from date with comma(,)
            date = ",".join(date)
            months = date.split("-")

            profit_loss = row[1]

        # Increment the counter to calculate total number of months
            count = count + 1
        
        # Calculate total profit or loss
            totalPL = totalPL + int(profit_loss)
        
        #Calculate Difference  in profit or loss in current and previous row 
            prevDiff = int(profit_loss) - prevPL

        # Max Increase
            if prevDiff>maxInc:
                maxInc = prevDiff
                maxIncMonth = row[0]


        # Max Decrease
            if prevDiff<maxDec:
                maxDec = prevDiff
                maxDecMonth = row[0]

        # Difference Total
            diffTotal = diffTotal + prevDiff
            if(count == 1):
                diffTotal =0

            prevPL = int(profit_loss)
    
    # Calculating the output to display analysis output
    output1 = ("Financial Analysis" + "\n" + "----------------------------")
    output2 = "Total Months: " + str(count)
    output3 = "Total: $" + str(totalPL)
    output4 = "Average  Change: $" + str(diffTotal/(count-1))
    output5 = "Greatest Increase in Profits: " + maxIncMonth + " ($" +str(maxInc)+ ")" 
    output6 = "Greatest Decrease in Profits: " + maxDecMonth + " ($" + str(maxDec)+ ")"
    
    # Printing the output on screen
    print(output1)    
    print(output2)    
    print(output3)
    print(output4)
    print (output5)
    print (output6)
    
    # Writing in output file output_budget_file
    out_file.write(output1 + "\n")
    out_file.write(output2 + "\n")
    out_file.write(output3 + "\n")
    out_file.write(output4 + "\n")
    out_file.write(output5 + "\n")
    out_file.write(output6 + "\n")


        