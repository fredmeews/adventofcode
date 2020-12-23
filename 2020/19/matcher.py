import re

#with open('input.txt') as f:
#passports = [x.strip() for x in f.readlines()]

rules = {}
QQ = "\""
OR = "|"

def quote(s):
    return QQ + s + QQ

def addRule(id, regex):
    rules[id] = regex
    print(rules)

def getRule(id):
    regex = ""

    for s in rules[id].split():
        if s.isalpha():
            regex += s
            break

        print("S = {}".format(s))
        if s.isnumeric():
            regex += getRule( int(s) )
        elif s == OR:
            regex += OR

    print("RE = {}".format(regex))
    return regex
        

def match(ruleId, s):
    regex = getRule(ruleId)
    pattern = re.compile( regex )

    print ("matching {} against {}".format(s, regex))
    return (pattern.match( s ))
