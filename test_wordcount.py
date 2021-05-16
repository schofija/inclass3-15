import unittest
import wordcount

#pytest
def test_wordcount_2_pytest():
    assert wordcount.count("Hello world") == 2 #testing basic functionality
def test_wordcount_4_pytest():
    assert wordcount.count("this is a test                    ") == 4 #testing if program still works if numerous spaces are added to the end of a string
def test_emptypytest():
    assert wordcount.count("") == 0 #testing if program works if input is empty
    
#unittest
class testwordcount(unittest.TestCase):
    def test_wordcount_2(self):
        self.assertEqual(wordcount.count("                  Hello world"), 2) #testing if adding spaces @ start of string changes output
    def test_wordcount_1(self):
        self.assertEqual(wordcount.count("   Hey   "), 1) #testing if putting spaces around a single word changes word count
    def test_onlyspace(self):
        self.assertEqual(wordcount.count("  "), 0) #testing if input of only spaces gives a proper output