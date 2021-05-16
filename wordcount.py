
#wordcount.py
#takes string input. returns word count

def count(string1):
    wordcount = 0
    for i in range(0, len(string1)):
        if string1[i] == " ":
            wordcount += 1
    if len(string1) != 0:    
        if string1[len(string1) - 1] != " ":
            wordcount = wordcount + 1
    return wordcount

        
