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



class TestPart2WTF(unittest.TestCase):
    def setUp(self):
        matcher.init()
        matcher.readRulesFile("testinputRules.txt")

    #start by looking at which rules ALWAYS match the same set of values and
    # how those rules (especially rules 42 and 31)
    # are used by the new versions of rules 8 and 11.
    #
    def testDebugPatterns(self):
        matcher.PARTIAL_MATCH = True

        for rule in [8,11]:
            matcher.match(rule,"aaaaabbaabaaaaababaa")  # 9. USE THIS ONE


    def testPartTwo(self):
        # Override rules 8, 11 - children of root match "0"
        # 0: 8 11
        matcher.addRule(8, "42 | 42 8")
        matcher.addRule(11, "42 31 | 42 11 31")

        self.assertTrue (matcher.match(0, "bbabbbbaabaabba"))
        self.assertTrue (matcher.match(0, "babbbbaabbbbbabbbbbbaabaaabaaa"))
        self.assertTrue (matcher.match(0, "aaabbbbbbaaaabaababaabababbabaaabbababababaaa"))
        self.assertTrue (matcher.match(0, "bbbbbbbaaaabbbbaaabbabaaa"))
        self.assertTrue (matcher.match(0, "bbbababbbbaaaaaaaabbababaaababaabab"))
        self.assertTrue (matcher.match(0, "ababaaaaaabaaab"))
        self.assertTrue (matcher.match(0, "ababaaaaabbbaba"))
        self.assertTrue (matcher.match(0, "baabbaaaabbaaaababbaababb"))
        self.assertTrue (matcher.match(0, "abbbbabbbbaaaababbbbbbaaaababb"))
        self.assertTrue (matcher.match(0, "aaaaabbaabaaaaababaa"))
        self.assertTrue (matcher.match(0, "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa"))
        self.assertTrue (matcher.match(0, "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"))
    
if __name__ == '__main__':
    unittest.main()
