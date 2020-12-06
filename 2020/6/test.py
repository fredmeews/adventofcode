import unittest
import customs

class TestSolution1(unittest.TestCase):
    def test_solution1Example(self):
        questions = customs.solution1("testinput.txt")
        self.assertEqual( questions, 11 )

    def test_solution1(self):
        questions = customs.solution1("input.txt")

class TestSolution2(unittest.TestCase):
    def test_solution2Example(self):
        questions = customs.solution2("testinput.txt")
        self.assertEqual( questions, 6 )        

    def test_solution2(self):
        questions = customs.solution2("input.txt")
        


        

    
if __name__ == '__main__':
    unittest.main()
