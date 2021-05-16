string1 = input("Please input a string. The program will then tell you if your string is a palindrome: ")
string2 = string1 [::-1]

if string1 == string2:
    print("***Your string is a palindrome!***")
    quit()
else:
    print("Not a palindrome")