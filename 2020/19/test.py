# Unit tests [https://docs.python.org/3/library/unittest.html]
# ============================================================
#   python3 -m unittest test
#   python3 -m unittest test.TestRows
#   python3 -m unittest test.TestRows.test_example1Row

import unittest
import matcher

class TestMatch(unittest.TestCase):
    def setUp(self):
        matcher.init()
        
    def test_matchLetterRule(self):
        matcher.addRule(0, "a")
        self.assertTrue( matcher.match(0, "a"))
        self.assertFalse( matcher.match(0, "b"))

    def test_getRegex(self):
        matcher.addRule(0, "1")        
        matcher.addRule(1, "2")
        matcher.addRule(2, "a")
        self.assertEqual( matcher.getRegex(0), "((a))")

    def test_getRegex2(self):
        matcher.addRule(0, "1")        
        matcher.addRule(1, "2 3")
        matcher.addRule(2, "a")
        matcher.addRule(3, "b")                
        self.assertEqual( matcher.getRegex(0), "((ab))" )

    def test_getRegex2_1(self):
        matcher.addRule(0, "1")        
        matcher.addRule(1, "3 2")
        matcher.addRule(2, "a")
        matcher.addRule(3, "b")                
        self.assertEqual( matcher.getRegex(0), "((ba))" )

    def test_getRegexWithOr(self):
        matcher.addRule(0, "1")        
        matcher.addRule(1, "2 3 | 3 2")
        matcher.addRule(2, "a")
        matcher.addRule(3, "b")

        self.assertEqual( matcher.getRegex(0), "((ab|ba))" )                

    def test_matchWithOr(self):
        matcher.addRule(0, "1")        
        matcher.addRule(1, "2 3 | 3 2")
        matcher.addRule(2, "a")
        matcher.addRule(3, "b")

        self.assertTrue( matcher.match(0, "ab" ))
        self.assertTrue( matcher.match(0, "ba" ))

    def testReadRulesFile(self):
        matcher.readRulesFile("testinput.txt")
        self.assertTrue( matcher.match(0, "aaaabb" ))
        self.assertTrue( matcher.match(0, "abbbab" ))        
        
        self.assertFalse(matcher.match(0, "bababa"))
        self.assertFalse(matcher.match(0, "aaaabbb"))        
        self.assertFalse(matcher.match(0, "aaabbb"))        


        
#    def test_matchReferenceRule(self):

    
if __name__ == '__main__':
    unittest.main()
