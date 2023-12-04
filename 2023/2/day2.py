import re

# Game, set, round

# MAIN
max = { 'red' : 12, 'green' : 13, 'blue' : 14 }

idSum = 0
maxGame = {}
with open('input.txt') as f:
    for game in f:
        gameNo = int (game.split(":")[0].split("Game ")[1])
        gameSets = game.split(": ")[1].split(";")

        print("GAME: %d" % gameNo)
        maxGame = { 'red' : 0, 'green' : 0, 'blue' : 0 }        
        for set in gameSets:
#            print("\tSET-- [%s]" % set.strip())                
            for round in set.split(","):
                cube = round.strip().split()
#                print("\t\tCUBE: [%s]" % cube)
                n = int(cube[0])
                if n > maxGame[ cube[1] ]:
                    maxGame[ cube[1] ] = int(cube[0])

        print(maxGame)
        if maxGame[ 'blue' ] <= max[ 'blue' ] and maxGame[ 'green' ] <= max[ 'green' ] and maxGame[ 'red' ] <= max[ 'red' ]:
            idSum = idSum + gameNo

print("SUM: %d " % idSum)
            
