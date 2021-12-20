import re

class Password:
    def __init__(self, min, max, letter, password):
        self.min = min
        self.max = max
        self.letter = letter
        self.password = password

    def isValid_one(self):
        letterCount = 0
        for ch in self.password:
            if ch == self.letter:
                letterCount = letterCount + 1

        valid = True
        if letterCount < self.min or letterCount > self.max:
            valid = False

        print ("DEBUG: count = {0}, letter = {1}, result = {2}".format(letterCount, self.letter, valid)) 
        return valid

    def isValid_two(self):
        # Adjust for zero index
        pos1 = self.min - 1
        pos2 = self.max - 1

        valid = False
        if (self.password[ pos1 ] == self.letter or self.password[ pos2 ] == self.letter) and \
           not(self.password[ pos1 ] == self.letter and self.password[ pos2 ] == self.letter):
            valid = True
            
        print ("DEBUG: pos1 = {0}, pos2 = {1}, result = {2}".format(pos1, pos2, valid))
        return valid    
    
# ---- MAIN
valid = 0
with open('input.txt') as f:
    for line in f:
        # "Input format: 1-3 a: abcde"
        l2 = re.sub(r'(\d+)\-(\d+)\s(\S): (\S+)\n', r'\1,\2,\3,\4', line)
        (min, max, letter, password) = l2.split(",")
        
        print ("DEBUG" , (min, max, letter, password))
        p = Password(int(min), int(max), letter, password)
        if p.isValid_two() == True:
            valid = valid + 1

    print("%d valid passwords\n" % valid)
