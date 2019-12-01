import os
#Initializing the variables declared
count = 0
months_list = []
total= 0
prevPL = 0
diff = 0
diffTotal =0
maxInc = 0
maxIncMonth = 'NULL'
maxDec = 0
maxDecMonth = 'NULL'

#Setitng the filepath for csv file budget_data.csv
filepath = os.path.join("Resources", "budget_data.csv")
filepath_output = os.path.join("Resources", "output_budget_file.txt")

#Opening the file in read mode
with open(filepath_output, "w+") as out_file:

#Opening the file in read mode
    with open (filepath, "r") as file:
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
        
        #Calculate total profit or loss
            total = total + int(profit_loss)
        
        #diff = prevPL - int(profit_loss)

        #Max Increase
            prevDiff = int(profit_loss) - prevPL
            if prevDiff>maxInc:
                maxInc = prevDiff
                maxIncMonth = row[0]


        #Max Decrease
            if prevDiff<maxDec:
                maxDec = prevDiff
                maxDecMonth = row[0]

        #diff total
            diffTotal = diffTotal + prevDiff
            if(count == 1):
                diffTotal =0

            prevPL = int(profit_loss)
    output1 = "Total Months: " + str(count)
    output2 = "Total: $" + str(total)
    output3 = "Average  Change: $" + str(diffTotal/(count-1))
    output4 = "Greatest Increase in Profits: " + maxIncMonth + " ($" +str(maxInc)+ ")" 
    output5 = "Greatest Decrease in Profits: " + maxDecMonth + " ($" + str(maxDec)+ ")"

    print(output1)    
    print(output2)
    print(output3)
    print (output4)
    print (output5)
    out_file.write("Financial Analysis" + "\n")
    out_file.write("----------------------------------------------------" + "\n")
    out_file.write(output1 + "\n")
    out_file.write(output2 + "\n")
    out_file.write(output3 + "\n")
    out_file.write(output4 + "\n")
    out_file.write(output5 + "\n")


        