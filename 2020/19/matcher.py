import re

rules = {}
regexes = {}
PART=2
QQ = "\""
OR = "|"
CNT=0


def init():
    print("init")
    rules.clear()
    regexes.clear()

def addRule(id, rule):
    rules[id] = rule

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
                if not subId == id: # avoid infinite loop
                    regex += getRegex( subId )

        if PART == 1:
            regex += ")"
        else:
            regex += ")"
            if id == 42:
                regex += "+"
            elif id == 31:
                regex += "+" 

        regexes[id] = regex
    return regexes[id]


def match(ruleId, s):
    regex = getRegex(ruleId)
    pattern = re.compile( regex )

    m = pattern.fullmatch( s )
    if (m == None):
        print("\t==> NO MATCH")
    return (m != None)


def readRulesFile(filename):
    with open(filename) as f:
        for line in f:
            if line.strip() and not line[0] == "#":
                (key, val) = line.strip().split(": ")
                addRule(int(key), val.strip(QQ))

def main():
    init()
    readRulesFile("inputRules.txt")

    if PART == 2: # modify 2 rules
        addRule(8, "42 | 42 8")
        addRule(11, "42 31 | 42 11 31")
    
    matches = 0
    with open("inputMatches.txt") as f:
        for line in f:
            if match( 0, line.strip() ):
                matches += 1
                print ("MATCHED: {}\n----------------\n".format(line.strip()))

    print("MATCHES: {}".format(matches))

if __name__ == '__main__':
    main()
