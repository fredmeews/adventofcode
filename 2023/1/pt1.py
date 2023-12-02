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

# ---- MAIN
sum = 0
with open('input.txt') as f:
    for line in f:
        match = re.findall(r'\d', line)        
        first = match[ 0 ][ 0 ]

        if not first.isdigit():
            first = numbers[ first ]

        last = match[ match.__len__() - 1 ][ 0 ]
        if not last.isdigit():
            last = numbers[ last ]
        
        value = str(first) + str(last)
        sum = sum + int(value)
        print(line, value, sum)

    print("TOTAL: %d" % sum)
