import re

rules = {}
regexes = {}
SAW = {}
PARTIAL_MATCH = False
QQ = "\""
OR = "|"
CNT=0


def init():
    print("init")
    rules.clear()
    regexes.clear()
    SAW = { 42 : False, 31 : False }
    PARTIAL_MATCH = False

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

        # Part 2 - these special rules get a "+" regex modifier
        regex += ")+" if id == 42 or id == 31 else ")"
        #regex += ")"   # PART 1
        
        regexes[id] = regex

#        if (id == 8 or id == 11):
#            print ("{}: {}".format(id, regex))
            
    return regexes[id]

def toBin(s):
    return s.replace("a", "0").replace("b", "1")

def match(ruleId, s):
    regex = getRegex(ruleId)
    pattern = re.compile( regex )

    #DEBUG
    m = None
    
    if PARTIAL_MATCH == True:
        #        m = pattern.search( s )
        m = pattern.findall( s )        
        print("\n\nID: {}, {}".format(ruleId, regex), end = " => ")
        for tuple in m:
            for str in tuple: 
                if str:
                    print(str, end=",")
        print(" IN [{}]".format(s))
        
    else:
        m = pattern.fullmatch( s )

    global CNT
#    print ("===ID: {}, INPUT: {} ".format(ruleId, CNT))
#    CNT += 1
    if (m == None):
        print("\t==> NO MATCH")
    # elif (m != None):
    #     bin = toBin(m[0])
    #     print ("\t==> {} => {} => {} subst in [{}]".format(int(bin, 2), bin, m[0], s ))
    #     #        print ("ID: {} => {} subst in [{}]".format(ruleId, m, s))
        
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
    
    matches = 0
    with open("inputMatches.txt") as f:
        for line in f:
            if match( 0, line.strip() ):
                matches += 1
                print ("MATCHED: {}\n----------------\n".format(line.strip()))

    print("MATCHES: {}".format(matches))

if __name__ == '__main__':
    main()
