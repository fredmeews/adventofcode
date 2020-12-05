import unittest
import seating

class TestMisc(unittest.TestCase):
    def test_loadFile(self):
        instructions = seating.loadFile("testinput.txt")
        print(instructions)
        self.assertEqual(len(instructions), 4)


class TestRows(unittest.TestCase):
    def test_frontRow(self):
        row = seating.findRow("FFF", 0, 7)
        self.assertEqual(row, 0)

    def test_backRow(self):        
        row = seating.findRow("BBB", 0, 7)
        self.assertEqual(row, 7)

    def test_example1Row(self):
        row = seating.findRow("FBFBBFF", 0, 127)
        self.assertEqual(row, 44)

    def test_example2Row(self):
        row = seating.findRow("BFFFBBFRRR", 0, 127)
        self.assertEqual(row, 70)

    def test_example3Row(self):
        row = seating.findRow("FFFBBBFRRR", 0, 127)
        self.assertEqual(row, 14)                

    def test_example4Row(self):
        row = seating.findRow("BBFFBBFRLL", 0, 127)
        self.assertEqual(row, 102)

class TestCols(unittest.TestCase):
    def test_leftCol(self):
        col = seating.findCol("LLL", 0, 7)
        self.assertEqual(col, 0)

    def test_rightCol(self):        
        col = seating.findCol("RRR", 0, 7)
        self.assertEqual(col, 7)

    def test_example1(self):        
        col = seating.findCol("FBFBBFFRLR", 0, 7)
        self.assertEqual(col, 5)

class TestSeat(unittest.TestCase):
    def test_example1(self):
        seat = seating.findSeat("FBFBBFFRLR")
        self.assertEqual(seat, 357)
    
if __name__ == '__main__':
    unittest.main()
