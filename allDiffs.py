import squareBoard

board_length = 9

def searchForSingles(allDiff):
    singles = []
    for x in range(board_length):
        # print(allDiff[x].domain)
        if len(allDiff[x].domain) == 1:
            singles.append(allDiff[x].domain[0])
    return singles

def changeDomainofSquares(allDiff, values, exceptions):
    for x in range(board_length):
        # print ('before' + str(allDiff[x].domain))
        for i in range(len(values)):
            if len(allDiff[x].domain) != 1:
                if len(exceptions) > 0:
                    if allDiff[x].domain != exceptions[0].domain:
                        #if domain of cell == domain of exception
                        allDiff[x].remove(values[i])
                else:
                    allDiff[x].remove(values[i])