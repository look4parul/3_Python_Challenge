import os   
# Declaring and Initializing the variables 
word_count = dict()
total_words = 0
sentences = 0
blanklines = 0
lines = 0
characters = 0
words = ""
line_sum=0

## Set the filepath for the input file (paragraph.txt) 
filepath_input = os.path.join("raw_data", "paragraph.txt")
## Set the filepath for the output file output_file.txt 
filepath_output = os.path.join("raw_data", "output_file.txt")

# Open the ouput file in write mode
with open(filepath_output, "w+") as out_file:
    #Open the input file (paragraph.txt) in read mode
    with open (filepath_input, "r") as in_file:
        for line in in_file:
        # Ignoring special characters (. , "", : , ' and ,) in each row while counting words
            line = line.replace(",", "").replace(".","").replace('""', "").replace(":", "").replace("'", " ").replace("-"," ")
            row = line.strip().split(" ")
        
            # Counter to count the number of words in a row: 
            for row_elem in row:
                if row_elem in word_count:
                    word_count[row_elem] +=1
                else:
                    word_count[row_elem] = 1
        
        # Calculating average nmber of lines
        for k,v in word_count.items():
            total_words = total_words + v
        output1 = "Approximate Word Count is: " + str(total_words)
        print(output1)

    # Count the number of sentences          
    with open (filepath_input, "r") as in_file:
        for line in in_file:
            #Checking for blank lines
            if line.startswith('\n'):
                blanklines += 1
            else:
        # Assume that each sentence ends with . or ! or ? and count these characters to claculate the number of sentences
                sentences += line.count('.') + line.count('!') + line.count('?')
        output2 = "Approximate Sentence Count: " + str(sentences)
    print (output2)    

    with open (filepath_input, "r") as in_file:
        for line in in_file:
            row = line.strip().split()
            # Calculating the number of characters
            characters = characters + len(line.replace(" ",""))
            #Average Letter count = Total number of characters / Total Number of lines
            avg_letter_count = (characters/total_words)
            #Average Sentence Length = Total number of lines / Sentence count
            avg_sentence_length = (total_words/sentences)
    #_____________ Printing the putput 
    output3 = "Average Letter Count: " + str(avg_letter_count)
    print(output3)
    output4 = "Average Sentence length: " + str(avg_sentence_length)
    print(output4)

    
    # _______________________ Writing in the output file

    out_file.write(output1 + "\n")
    out_file.write(output2 + "\n")
    out_file.write(output3 + "\n")
    out_file.write(output4 + "\n")

