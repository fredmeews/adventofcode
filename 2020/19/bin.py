with open('testinputMatches2-bin.txt') as f:
    for line in f.readlines():
        line = line.strip()
        if line and not line[0] == "#":
            print("{} ==> {}".format(line, int(line, 2)))
        else:
            print(line)

