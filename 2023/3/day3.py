import re

LINELEN=140

def checkForSymbol( start, end, line ):
#    print("checkForSymbol %d %d %s" % (start,end,line))

    for c in range(start, end):
#        print("checking: " + line[c])
        ascii = ord(line[c])
        # Letters and period
        isNumber = (ascii >= 48 and ascii <= 57) or ascii == 46

        if not isNumber:
            return True

    return False


# MAIN
lineAbove = ""
lineBelow = ""
line = ""

row = 0
lineNum = 0
eof = False
partNumSum = 0
with open('input.txt') as f:
    lineAbove = f.readline().strip()
    currLine = f.readline().strip()
    lineBelow = f.readline().strip()
        
    while not eof:
#        print("------------------------------")            
#        print("\tLINE: " + lineAbove)
#        print("\tLINE: " + currLine + "<<<<")
#        print("\tLINE: " + lineBelow)        
        
        for m in re.finditer(r'\d+', currLine):
            partNum = int (currLine[m.start(0) : m.end()])
#            print ("\tMATCH: " + currLine[m.start(0) : m.end()])
            
            start = m.start()
            if m.start() > 0:
                start = start - 1
                
            end = m.end()
            if m.end() < LINELEN-1:
                end = end + 1
                    
            #        print("check above: %d %d %s" % (start,end, line[m.start():m.end()]))
            b = checkForSymbol( start, end, lineAbove )
#            print("\tABOVE %s: %s" % (currLine[m.start():m.end()], b))

            if b == False:
                b = checkForSymbol( start, end, lineBelow )
 #               print("\tBELOW %s: %s" % (currLine[m.start():m.end()], b))

            if b == False:
                b = checkForSymbol( start, end, currLine )
  #              print("\tCURR%s: %s" % (currLine[m.start():m.end()], b))                

            if b == True:
                print("%d " % (partNum), end = " ")
                partNumSum = partNumSum + partNum

        # Shift down
        lineAbove = currLine
        currLine = lineBelow
        lineBelow = f.readline().strip()
        print("")

        if lineBelow == '':
            eof = True

    print("SUM: %d " % partNumSum)
