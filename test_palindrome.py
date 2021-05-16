import unittest
import palindrome

#pytest
def test_NotPalindromepytest():
    assert palindrome.palindrome("Hello world") == 0
def test_Palindromepytest():
    assert palindrome.palindrome("tacocat") == 1
def test_emptypytest():
    assert palindrome.palindrome("") == 0
    
#unittest
class testPalindrome(unittest.TestCase):
    def test_NotPalindrome(self):
        self.assertEqual(palindrome.palindrome("Hello world"), 0)
    def test_Palindrome(self):
        self.assertEqual(palindrome.palindrome("TACOCAT"), 1)
    def test_empty(self):
        self.assertEqual(palindrome.palindrome(""), 0)
        
        
#if __name__ == '__main__':
#    unittest.main()