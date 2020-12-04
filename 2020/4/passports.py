import re

with open('input.txt') as f:
    passports = [x.strip() for x in f.readlines()]

def validateField(key, val):
    valid = True
    
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if key == "byr":
        val = int(val)
        valid = val >= 1920 and val <= 2002

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    elif key == "iyr":
        val = int(val)        
        valid = val >= 2010 and val <= 2020

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    elif key == "eyr":
        val = int(val)
        valid = val >= 2020 and val <= 2030

    # hgt (Height) - a number followed by either cm or in:
    elif key == "hgt":
        valid = False
        if re.match('\d+(in|cm)', val) is not None:
            tokens = re.sub(r'(\d+)(\S+)', r'\1:\2', val).split(":")
            n = int(tokens[0])
            unit = tokens[1]

            # If cm, the number must be at least 150 and at most 193.
            if unit == "cm":
                valid = n >= 150 and n <= 193
            # If in, the number must be at least 59 and at most 76.
            else:
                valid = n >= 59 and n <= 76

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    elif key == "hcl":
        valid = re.match('#[a-f0-9]{6,6}', val) is not None

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    elif key == "ecl":
        valid = (val in "amb blu brn gry grn hzl oth")
            
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    elif key == "pid":
        valid = re.match('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$', val) is not None

    if valid == False:
        print("\nfield error: {} = {} ==> {}".format(key, val, valid))
       
    return valid

def validatePassport(passport):
    required = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ]
    keys = []
    vals = []
    
    for pair in passport:
        tokens = pair.split(":")
        key, val = tokens[:-1], tokens[-1:]
        keys.extend(key)
        vals.extend(val)

    valid = True
    for field in required:
        try:
            i = keys.index(field)
            valid = validateField( keys[i], vals[i] )
            if valid == False:
                break

        except ValueError:
            print("\n{} is missing '{}'".format(keys, field))
            valid = False
            break

    print("PASSPORT: {} ==> {}".format(passport, valid))
    return valid

def validatePassports():
    p = []
    countValid = 0
    for line in passports:
        if (len(line) > 0):
            p.extend(line.split())
        else:
            countValid += validatePassport(p)
            p = []

    # edge case - last passport, clean this up
    countValid += validatePassport(p)
                
    return countValid
            
print ("{} are valid".format(validatePassports()))
