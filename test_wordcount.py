import unittest
import wordcount

#pytest
def test_wordcount_2_pytest():
    assert wordcount.count("Hello world") == 2
def test_wordcount_4_pytest():
    assert wordcount.count("this is a test                    ") == 4
def test_emptypytest():
    assert wordcount.count("") == 0
    
#unittest
class testwordcount(unittest.TestCase):
    def test_wordcount_2(self):
        self.assertEqual(wordcount.count("                  Hello world"), 2)
    def test_wordcount_1(self):
        self.assertEqual(wordcount.count("   Hey   "), 1)
    def test_onlyspace(self):
        self.assertEqual(wordcount.count("  "), 0)