# For a similar but more elegant solution:
# https://github.com/fuglede/adventofcode/blob/master/2020/day03/solutions.py
#

def isTree(x,y):
    y = y * rowLength  # Convert 1-d array to 2-d
    x = x % rowLength # Allow row to extend & repeat
    position = x + y
    return MAP[position]


# ------------- Read input as characters into a big list
rowLength = 0
MAP = []
with open('input.txt') as file:
    for line in file:
        line = line.rstrip("\n")
        if (rowLength == 0):
            rowLength = len(line)

        for char in line:
            MAP.append(char == "#")

numRows = int(len(MAP) / rowLength)

# ------------ MAIN
SLOPES = [ [1,1], [3,1], [5,1], [7,1], [1,2] ];

solution = 1
for slope in SLOPES:
    x = 0
    y = 0
    trees = 0
    
    while True:
        x = x + slope[0] # right
        y = y + slope[1] # down
        if y > (numRows - 1):
            break

        if isTree(x,y) == True:
            trees = trees + 1

    print("DEBUG: for slope {},{}  trees = {}".format(slope[0], slope[1], trees))
    solution = solution * trees

print("SOLUTION: {}".format(solution))
