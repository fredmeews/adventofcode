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
    # id42 = "((b(a(bb|ab)|b((a|b)(a|b)))|a(b(bb)|a(bb|a(a|b))))b|(((aa|ab)a|(bb)b)b|(((a|b)a|bb)a)a)a)+"
    # id31 = "(b(b(a(ba)|b(aa))|a(b(ab|(a|b)a)|a(ba|ab)))|a(b((ab|(a|b)a)b|((a|b)a|bb)a)|a((ba)b|(ba|bb)a)))*"

    # if id == 0:
    #     return "(" + id42 + id31 + ")"
    # REPEAT = "+"

    # # (8, "42 | 42 8")    
    # if id == 8:
    #     left = id42
    #     right = id42
    #     loop = "(" + left + right + ")" + REPEAT
    #     return "(" + left + OR + loop + ")"

    # # (11, "42 31 | 42 11 31")
    # # (11, "42 31 | 42 (42 31 | 42+ 31) 31")    
    # elif id == 11:
    #     left = id42 + id31
    #     return "(" + left + OR + id42 + "(" + left + ")" + REPEAT + id31 + ")"

    
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
                # if PART == 2 and subId == id: # recursion
                #     regex += "(" + regex + ")*)"
                #     print("SUB: {} => {}".format(subId, regex))
                # else:
                regex += getRegex( subId )
                    
        regex += ")"
        regexes[id] = regex

#        print("RE: {} => {}".format(id, regexes[id]))        
    return regexes[id]


def match(ruleId, s):
    regex = getRegex(ruleId)
    pattern = re.compile( regex )
    print ("======\n{} => {}".format(ruleId, s))

    m = pattern.fullmatch( s )
    if (m == None):
        print("\t==> NO MATCH")
    else:
        print(m)
    return (m != None)

def match0(zero, s):
    m42 = re.compile( getRegex(42) )
    m31 = re.compile( getRegex(31) )

    ######### 42
    pos = 0
    print("trying 42.1 {}".format(s))                     
    go42 = len(s) > 0
    while go42 == True: 
        if len(s) > 0:
            m = m42.match(s)
            print("41.1 {} against {}".format(m, s))
            if m == None:
                go42 = False
            else:
                pos = len(m[0])
                s = s[pos:]
        else:
            go42 = False

    ######### 31
    pos = 0
    cnt = 0
    go31 = len(s) > 0
    while go31 == True:
        cnt += 1
        print("trying 31 {}".format(s))                     
        if len(s) > 0:
            m = m31.match(s)
            print("31.0 {} against {}".format(m, s))            
            if m == None:
                go31 = False
            else:
                pos = len(m[0])
                s = s[pos:]
        else:
            go31 = False

    # ######### 42
    # pos = 0
    # print("trying 42.2 {}".format(s))                     
    # go42 = len(s) > 0
    # while go42 == True: 
    #     if len(s) > 0:
    #         m = m42.match(s)
    #         print("41.2 {} against {}".format(m, s))
    #         if m == None:
    #             go42 = False
    #         else:
    #             pos = len(m[0])
    #             s = s[pos:]
    #     else:
    #         go42 = False
            
    return (len(s) == 0)
            




def readRulesFile(filename):
    with open(filename) as f:
        for line in f:
            if line.strip() and not line[0] == "#":
                (key, val) = line.strip().split(": ")
                addRule(int(key), val.strip(QQ))

def main():
    init()
    readRulesFile("inputRules.txt")

    # if PART == 2: # modify 2 rules
    #     addRule(8, "42 | 42 8")
    #     addRule(11, "42 31 | 42 11 31")
    
    matches = 0
    with open("inputMatches.txt") as f:
        for line in f:
            if match0( 0, line.strip() ):
                matches += 1
                print ("MATCHED: {}\n----------------\n".format(line.strip()))
            else:
                print ("NOT MATCHED: {}\n----------------\n".format(line.strip()))

    print("MATCHES: {}".format(matches))

if __name__ == '__main__':
    main()
