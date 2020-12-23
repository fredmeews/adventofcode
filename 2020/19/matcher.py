import re

rules = {}
QQ = "\""
OR = "|"

def quote(s):
    return QQ + s + QQ

def addRule(id, regex):
    rules[id] = regex

def getRule(id):
    regex = "("

#    print("ID = {}, {}".format(id, rules))

    for s in rules[id].split():
        if s.isalpha():
            regex += s
            return regex.strip("(")
        elif s == OR:
            regex +=  OR 
        elif s.isnumeric():
            regex += getRule( int(s) )

#    print("RE = {}".format(regex))
    return regex + ")"
        

def match(ruleId, s):
    regex = getRule(ruleId)
    pattern = re.compile( regex )

#    print ("matching {} against {}".format(s, regex))
    return (pattern.fullmatch( s ) != None)

def readRulesFile(filename):
    with open(filename) as f:
        for line in f:
            (key, val) = line.strip().split(": ")
            addRule(int(key), val.strip(QQ))


def main():
    readRulesFile("inputRules.txt")
    
    matches = 0
    with open("inputMatches.txt") as f:
        for line in f:
            if match( 0, line.strip() ):
                matches += 1

    print("MATCHES: {}".format(matches))

if __name__ == '__main__':
    main()
