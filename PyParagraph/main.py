import os   
word_count = dict()
sum = 0
sentences = 0
blanklines = 0
lines = 0
characters = 0
words = ""
line_sum=0

## Set the filepath for the input file and output file
filepath_input = os.path.join("raw_data", "paragraph_3.txt")
filepath_output = os.path.join("raw_data", "output_file.txt")

# Open the ouput file(output_file.txt) in write mode
#with open(filepath_output, "w+") as out_file:
    #Open the input file (paragraph.txt) in read mode
with open (filepath_input, "r") as in_file:
    for line in in_file:
        # Ignoring special characters (. , "" and :) in each row while counting words
        line = line.replace(",", "").replace(".","").replace('""', "").replace(":", "").replace("'", " ").replace("-"," ")
        row = line.strip().split(" ")
        
        #words = len(line)
        
        # Print all the lines in the files
        #print(line)
        #print (row)
        # Counter to count the number of words in a row: 
        for row_elem in row:

            if row_elem in word_count:
                word_count[row_elem] +=1
            else:
                word_count[row_elem] = 1
        ## Calculating average nmber of lines

    for k,v in word_count.items():
## Print count of each word in a list
            #print (k, v)  
            # Number of words in a row
        sum = sum + v
        #output1 = "Approximate Word Count is: " + str(sum) + "\n"
    print("Approximate Word Count is: " , sum)

## Print word count for each line            
            #print(len(word))
    with open (filepath_input, "r") as in_file:
    #next(file)
        for line in in_file:
        # Ignoring (. , , ;) and \n in each row while counting words
        #row = line.strip().split(" ")        
        #lines +=1
            #Checking for blank lines
            if line.startswith('\n'):
                blanklines += 1
            else:
    # Assume that each sentence ends with . or ! or ?
    # so simply count these characters
                sentences += line.count('.') + line.count('!') + line.count('?')
        #output2 = "Approximate Sentence Count: " + str(sentences) + "\n"
    print ("Approximate Sentence Count: ", sentences)    

    with open (filepath_input, "r") as in_file:
        for line in in_file:
            row = line.strip().split()
            characters = characters + len(line.replace(" ",""))
            avg_letter_count = (characters/sum)
            avg_sentence_length = (sum/sentences)
#print(characters)
    #output3 = "Average Letter Count: " + str(avg_letter_count) + "\n"
    print("Average Letter Count: " + str(avg_letter_count))
    #output4 = "Average Sentence length: " + str(avg_sentence_length) + "\n" 
    print("Average Sentence length: " + str(avg_sentence_length))

    
    
    #out_file.write(output1)  
    #out_file.write(output2) 
    #out_file.write(output3) 
    #out_file.write(output4) 

