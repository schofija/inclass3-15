def palindrome(s):
    s2 = s [::-1]
    if len(s) == 0:
        print("Not a palindrome")
        return 0

    if s == s2:
        print("***Your string is a palindrome!***")
        return 1
    else:
        print("Not a palindrome")
        return 0
        
string1 = input("Please input a string. The program will then tell you if your string is a palindrome: ")   
palindrome(string1)     
