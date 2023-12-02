import re

numbers = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

def findLast(line):
    # Find last digit
    lastDigitIdx = -1
    for x in range(1, 10):
        idx = line.rfind( str(x) )
        if idx > lastDigitIdx:
            lastDigitIdx = idx
            print("Last digit %s at %d\n" % (line[lastDigitIdx], lastDigitIdx))

    # Find last word
    lastWordIdx = -1
    lastWord = ""
    for x in numbers.keys():
        idx = line.rfind( x )
        if idx > lastWordIdx:
            lastWordIdx = idx
            lastWord = x
            print("Last word %s at %d\n" % (lastWord, lastWordIdx))

    # Take the later one
    if lastDigitIdx > lastWordIdx:
        result = line[lastDigitIdx]
    else:
        result = int ( numbers[lastWord] )

    return str(result)

def findFirst(line):
    # Find first digit
    firstDigitIdx =  99999
    for x in range(1, 10):
        idx = line.find( str(x) )
        if idx > -1 and idx < firstDigitIdx:
            firstDigitIdx = idx
            print("First digit %s at %d\n" % (line[firstDigitIdx], firstDigitIdx))

    # Find first word
    firstWordIdx = 99999
    firstWord = ""
    for x in numbers.keys():
        idx = line.find( x )
        if idx > -1 and idx < firstWordIdx:
            firstWordIdx = idx
            firstWord = x
            print("First word %s at %d\n" % (firstWord, firstWordIdx))

    # Take the earlier one
    if firstDigitIdx < firstWordIdx:
        result = line[firstDigitIdx]
    else:
        result = int ( numbers[firstWord] )

    return str(result)


# MAIN
sum = 0
with open('input.txt') as f:
    for line in f:
        value = findFirst(line) + findLast(line)
        sum = sum + int(value)

print("SUM: %d" % sum)        

# TEST
#result = findFirst("two1nine")
#print(result)
