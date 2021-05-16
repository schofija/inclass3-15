string1 = input("Enter a string. This program will return the word count of said string: ")
wordcount = 0

for i in range(0, len(string1)):
    if string1[i] == " ":
        wordcount += 1
if len(string1) != 0:    
    if string1[len(string1) - 1] != " ":
        wordcount = wordcount + 1

print(wordcount, " words.")
        
