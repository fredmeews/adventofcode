import re

rules = {}
regexes = {}
QQ = "\""
OR = "|"

SAW = { 42 : False, 31 : False }

def quote(s):
    return QQ + s + QQ

def addRule(id, regex):
    rules[id] = regex

def getRegex(id):
    if not id in regexes:
        regex = "("
        for s in rules[id].split():
            if s.isalpha():
                regex += s
                return regex.strip("(")
            elif s == OR:
                regex +=  OR
            elif s.isnumeric():
                subId = int(s)
                regex += getRegex( subId )            
        regex += ")"
        regexes[id] = regex

#        if (id == 8 or id == 11):
#            print ("{}: {}".format(id, regex))
            
    return regexes[id]
        

def match(ruleId, s):
    regex = getRegex(ruleId)
    pattern = re.compile( regex )

    #DEBUG
    m = pattern.match( s )
    if (m != None):
        print ("ID: {} => {}".format(ruleId, m))
        
    return (pattern.fullmatch( s ) != None)

def readRulesFile(filename):
    with open(filename) as f:
        for line in f:
            if line.strip() and not line[0] == "#":
                (key, val) = line.strip().split(": ")
                addRule(int(key), val.strip(QQ))


def main():
    readRulesFile("testinputRules.txt")
    
    matches = 0
    with open("testinputMatches.txt") as f:
        for line in f:
            if match( 0, line.strip() ):
                matches += 1
                print ("MATCHED: {}\n----------------\n".format(line.strip()))

    print("MATCHES: {}".format(matches))

if __name__ == '__main__':
    main()
