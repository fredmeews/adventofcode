import unittest
import matcher

class TestMatch(unittest.TestCase):
    def test_matchLetterRule(self):
        matcher.addRule(0, "a")
        self.assertTrue( matcher.match(0, "a"))
        self.assertFalse( matcher.match(0, "b"))

    def test_getRule(self):
        matcher.addRule(0, "1")        
        matcher.addRule(1, "2")
        matcher.addRule(2, "a")
        self.assertEqual( matcher.getRule(0), "a")

    def test_getRule2(self):
        matcher.addRule(0, "1")        
        matcher.addRule(1, "2 3")
        matcher.addRule(2, "a")
        matcher.addRule(3, "b")                
        self.assertEqual( matcher.getRule(0), "ab" )

    def test_getRule2_1(self):
        matcher.addRule(0, "1")        
        matcher.addRule(1, "3 2")
        matcher.addRule(2, "a")
        matcher.addRule(3, "b")                
        self.assertEqual( matcher.getRule(0), "ba" )

    def test_getRuleWithOr(self):
        matcher.addRule(0, "1")        
        matcher.addRule(1, "2 3 | 3 2")
        matcher.addRule(2, "a")
        matcher.addRule(3, "b")

        self.assertEqual( matcher.getRule(0), "ab|ba" )                

    def test_matchWithOr(self):
        matcher.addRule(0, "1")        
        matcher.addRule(1, "2 3 | 3 2")
        matcher.addRule(2, "a")
        matcher.addRule(3, "b")

        self.assertTrue( matcher.match(0, "ab" ))
        self.assertTrue( matcher.match(0, "ba" ))                                         

        
#    def test_matchReferenceRule(self):

    
if __name__ == '__main__':
    unittest.main()
