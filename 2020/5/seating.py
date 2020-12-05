import math
import bisect 


ROWS=127
COLS=7

def loadFile(fileName):
    with open(fileName) as f:
        return [x.strip() for x in f.readlines()]
        

def findRow(instruction, _min, _max):
    for op in instruction:
        rows = _max - _min
        
        if op == "F" :
            _max = math.floor(rows / 2) + _min
        elif op == "B":
            _min =  math.ceil(rows / 2) + _min
        else:
            print("invalid row op {} skipping".format(op))
            continue

        if _min != _max:
            findRow(instruction[1:], _min, _max)

    return _max

def findCol(instruction, _min, _max):
    for op in instruction:
        cols = _max - _min
        
        if op == "L" :
            _max = math.floor(cols / 2) + _min
            
        elif op == "R":
            _min =  math.ceil(cols / 2) + _min

        else:
            print("invalid col op {} skipping".format(op))
            continue

        if _min != _max:
            findCol(instruction[1:], _min, _max)

    return _max

def findSeat(instruction):
    row = findRow(instruction[:7], 0, ROWS)
    col =  findCol(instruction[7:], 0, COLS)
    return ((row * 8) + col)


def partOne():
    maxSeat = 0
    for instruction in loadFile("input.txt"):
        seat = findSeat( instruction )
        maxSeat = max(maxSeat, seat)        

    print("SOLUTION 1: {}".format(maxSeat))

def partTwo():
    seats = []
    for instruction in loadFile("input.txt"):
        seat = findSeat( instruction )
        bisect.insort(seats, seat)

    for seat in seats[1:len(seats)-1]:
        try:
            seats.index( seat - 1 )
        except:
            print("SOLUTION: {}".format(seat-1))

if __name__ == '__main__':
    partTwo()

    
    
