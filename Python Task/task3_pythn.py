def word_count(input_file,output_file):
    try:
        #reading the text file
        f = open(input_file,"r")
        text = f.read()

        #counting the words
        total_words = len(text.split())


        #writing the contents into a new file
        f = open(output_file, "w")
        f.write(f"Total number of words in sample file are : {total_words}.")
    
    except FileNotFoundError:
        print("No file exist")
        
word_count("speech.txt","Write_file.txt")

    



