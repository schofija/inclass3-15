def palindrome(s):
    s2 = s [::-1]
    if len(s) == 0:
        print("Not a palindrome")
        quit()

    if s == s2:
        print("***Your string is a palindrome!***")
        quit()
    else:
        print("Not a palindrome")
        
string1 = input("Please input a string. The program will then tell you if your string is a palindrome: ")   
palindrome(string1)     
