import re

with open('input.txt') as f:
    passports = [x.strip() for x in f.readlines()]


def validatePassport(passport):
    valid = True
    required = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ]

    for field in required:
        try:
            passport.index(field)
        except ValueError:
            print("{} is missing {}".format(passport, field))
            valid = False
            break

    return valid

def validatePassports():
    p = []
    countValid = 0
    for line in passports:
        # strip off prefix
        line = re.sub(r'(\S+):\S+', r'\1', line)

        if (len(line) == 0):
            if (validatePassport(p)):
                countValid += 1
            p = []
        else:
            p.extend(line.split())

    return countValid
            
            
print ("{} are valid".format(validatePassports()))
