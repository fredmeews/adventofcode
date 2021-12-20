cnt = 0
with open('testinputMatches.txt') as f:
    passports = [x.strip() for x in f.readlines()]
    for p in passports:
        if (len(p) % 5 == 0):
            print("{} => {}".format(len(p), p))
            cnt += 1

print(cnt)


            
