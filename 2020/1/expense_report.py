
def part_1():
    # for number n1 in list, find if n2 exists where n1+n2 = 2020
    currentIndex = 0
    for n1 in L:
        n2 = 2020 - n1
    
        try:
            if L.index( n2, currentIndex ):
                print ("PART 1: %d + %d = 2020, product = %d\n" % (n1, n2, n1*n2))
                break
        except ValueError:
            currentIndex = currentIndex + 1
        

def part_2():
    found = False
    
    # Eliminate numbers too large faster?
    L2 = sorted(L, reverse=True)

    # for number n1 in list, find if n2 exists where n1+n2 = 2020
    for index1, n1 in enumerate(L2):
        for index2, n2 in enumerate(L2[index1 + 1:]):     # slice notation https://stackoverflow.com/a/6148636
            sum12 = n1 + n2
            if sum12 >= 2020:
                continue

            #print ("DEBUG %d + %d = %d\n", n1, n2, n1+n2)

            n3 = 2020 - sum12
            try:
                if L.index( n3, index2 ):
                    print ("PART 2: %d + %d + %d = 2020, product = %d \n" % (n1, n2, n3, n1*n2*n3))
                    found = True
                    break
            except ValueError:
                pass

        if found == True:
            break
    
# ---- MAIN
with open('input.txt') as f:
    L = [int(line.rstrip()) for line in f]

part_1()
part_2()
