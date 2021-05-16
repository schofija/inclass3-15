import unittest
import palindrome

#pytest
def test_NotPalindromepytest():
    assert palindrome.palindrome("Hello world") == 0 #testing basic functionality of program
def test_Palindromepytest():
    assert palindrome.palindrome("tacocat") == 1 #testing basic functionality of program
def test_emptypytest():
    assert palindrome.palindrome("") == 0 #testing if program can recognize and empty input, which should not be considered a palindrome
    
#unittest
class testPalindrome(unittest.TestCase):
    def test_NotPalindrome(self):
        self.assertEqual(palindrome.palindrome("elephant"), 0) #testing basic functionality
    def test_Palindrome(self):
        self.assertEqual(palindrome.palindrome("race car"), 1) #testing if program can detect palindromes with spaces in them
    def test_empty(self):
        self.assertEqual(palindrome.palindrome("          "), 0) #testing if program can detect empty inputs that are only spaces
        
        
if __name__ == '__main__':
    unittest.main()