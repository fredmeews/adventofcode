import json

# anyone = no dups, use set
def solution1(fileName):
    with open(fileName) as f:
        data = f.read()

    solution = 0
    for group in data.split("\n\n"):
        passengers = group.count("\n") + 1
        questions = set()
        [questions.add(q) for q in group]

        if passengers > 1:
            questions.remove('\n')
        
        solution += len(questions) 

    print ("SOLUTION: {}".format(solution))
    return solution


# everyone = dup counter, use hash
def solution2(fileName):
    with open(fileName) as f:
        data = f.read()

    solution = 0
    for group in data.split("\n\n"):
        qcnt = 0
        questions = {}
        passengers = group.strip().count('\n') + 1  # strip last \n
        
        for q in group:
            questions[q] = questions[q] + 1 if q in questions  else 1

        for key in questions:
            if key != '\n' and questions[key] == passengers:
                solution += 1
                #print("DEBUG: {} passengers answered {}".format(passengers, key))

    print ("SOLUTION: {} passengers".format(solution))
    return solution

        
if __name__ == '__main__':
    solution2("input.txt")
