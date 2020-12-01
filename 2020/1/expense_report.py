with open('input.txt') as f:
    L = [int(line.rstrip()) for line in f]

# for number n1 in list, find if n2 exists where n1+n2 = 2020
currentIndex = 0
for n1 in L:
#    print ("DEBUG: %d \n" % n1)
    n2 = 2020 - int(n1)

    try:
        if L.index( n2, currentIndex ):
            print ("%d * %d = %d\n" % (n1, n2, n1*n2))
            break
    except ValueError:
        pass
