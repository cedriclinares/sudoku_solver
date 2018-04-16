import cell
import sys
import allDiffs
import copy

class squareBoard:

    def __init__(self):
        self.board = []
        self.board_length = 9
        self.allDiffsLen = 3
        self.checkAll = ((0,0), (1,3), (2,6), (3,1), (4,4), (5,7), (6,2), (7,5), (8,8))
        for y in range(self.board_length):
            row = [cell.Cell() for x in range(self.board_length)]
            self.board.append(row)

    def getExample(self, example):
        for x in range(self.board_length):
            for y in range(self.board_length):
                self.board[x][y].position = [x, y]
                if example[x][y] != 0:
                    self.board[x][y].domain = [example[x][y]]



    def getStartBoard(self):
        i = 0
        while i < self.board_length:
            row = raw_input('Enter numbers for row %d separated by commas: ' % i)
            if row == 'start':
                self.autoStart()
                break
            a_list = map(int, row.split(','))
            print(a_list)
            if len(a_list) != self.board_length:
                print('Invalid input!')
                continue
            for x in range(self.board_length):
                self.board[i][x].position = [i, x]
                if a_list[x] != 0:
                    self.board[i][x].domain = [a_list[x]]

            i += 1

    def autoStart(self):
        i = 0
        while i < self.board_length:
            for x in range(self.board_length):
                self.board[i][x].position = [i, x]
            i += 1

    def getAllDiffs(self, row, column):
        wholeRow = self.getRow(row)
        wholeColumn = self.getColumn(column)
        wholeSquare = self.getWholeSquare(row,column)
        allDiffs = []
        allDiffs.append(wholeRow)
        allDiffs.append(wholeColumn)
        allDiffs.append(wholeSquare)
        return allDiffs

    def getRow(self, row):
        a_row = []
        for x in range(self.board_length):
            a_row.append(self.board[row][x])
        return a_row

    def getColumn(self, column):
        a_column = []
        for x in range(self.board_length):
            a_column.append(self.board[x][column])
        return a_column

    def getWholeSquare(self, row, column):
        rowThird = self.rowThird(row)
        columnThird = self.columnThird(column)
        wholeSquare = self.findSquare(rowThird, columnThird)
        return wholeSquare

    def rowThird(self, row):
        #print('row ' + str(row))
        if (row >= 0) and (row <= 2):
            return 'left'
        elif (row >= 3) and (row <= 5):
            return 'middle'
        elif (row >= 6) and (row <= 8):
            return 'right'

    def columnThird(self, column):
        #print('column ' + str(column))
        if (column >= 0) and (column <= 2):
            return 'top'
        elif (column >= 3) and (column <= 5):
            return 'middle'
        elif (column >= 6) and  (column <= 8):
            return 'bottom'

    def findSquare(self, rowThird, columnThird):
        square = columnThird+rowThird
        squares = {
            'topleft' : [self.board[0][0], self.board[0][1], self.board[0][2], self.board[1][0], self.board[1][1],
                         self.board[1][2], self.board[2][0], self.board[2][1], self.board[2][2]],
            'topmiddle': [self.board[0][3], self.board[0][4], self.board[0][5], self.board[1][3], self.board[1][4],
                        self.board[1][5], self.board[2][3], self.board[2][4], self.board[2][5]],
            'topright': [self.board[0][6], self.board[0][7], self.board[0][8], self.board[1][6], self.board[1][7],
                        self.board[1][8], self.board[2][6], self.board[2][7], self.board[2][8]],
            'middleleft': [self.board[3][0], self.board[3][1], self.board[3][2], self.board[4][0], self.board[4][1],
                        self.board[4][2], self.board[5][0], self.board[5][1], self.board[5][2]],
            'middlemiddle': [self.board[3][3], self.board[3][4], self.board[3][5], self.board[4][3], self.board[4][4],
                        self.board[4][5], self.board[5][3], self.board[5][4], self.board[5][5]],
            'middleright': [self.board[3][6], self.board[3][7], self.board[3][8], self.board[4][6], self.board[4][7],
                        self.board[4][8], self.board[5][6], self.board[5][7], self.board[5][8]],
            'bottomleft': [self.board[6][0], self.board[6][1], self.board[6][2], self.board[7][0], self.board[7][1],
                        self.board[7][2], self.board[8][0], self.board[8][1], self.board[8][2]],
            'bottommiddle': [self.board[6][3], self.board[6][4], self.board[6][5], self.board[7][3], self.board[7][4],
                        self.board[7][5], self.board[8][3], self.board[8][4], self.board[8][5]],
            'bottomright': [self.board[6][6], self.board[6][7], self.board[6][8], self.board[7][6], self.board[7][7],
                        self.board[7][8], self.board[8][6], self.board[8][7], self.board[8][8]]
        }
        return squares[square]

    def solveNakedSingles(self):
        for i in range(self.board_length):
            for j in range(self.board_length):
                #print('On Square' + str(i) + ','  + str(j))
                #print('Domain: ' + str(self.board[i][j].domain))
                allDiff = self.getAllDiffs(i, j)
                for k in range(self.allDiffsLen):
                    singles = allDiffs.searchForSingles(allDiff[k])
                    singles2 = []
                    while singles != singles2:
                        singles2 = singles
                        allDiffs.changeDomainofSquares(allDiff[k], singles, [])
                        singles = allDiffs.searchForSingles(allDiff[k])
                        #If new single is discovered, repeat pruning

    def solveHiddenSingles(self):
        combinedDomain = []
        for i in range(self.board_length):
            allDiff = self.getAllDiffs(self.checkAll[i][0], self.checkAll[i][1])
            for j in range(self.allDiffsLen):
                for k in range(self.board_length):
                    # if len(allDiff[j][k].domain) == 1:
                    #     combinedDomain.append([-1]);
                    # else:
                    combinedDomain.append(allDiff[j][k].domain);
                print 'combined: ', combinedDomain
                index, value = self.findSingleValue(combinedDomain)
                if index != -1:
                    print 'index: ', index, 'value: ', value
                    print 'cell: ', allDiff[j][index]
                    allDiff[j][index].domain = [value]
                combinedDomain = []

    def findSingleValue(self, combinedDomain):
        occurences = [0,0,0,0,0,0,0,0,0]
        # count occurences of values in domains
        for i in range(self.board_length):
            for j in range(len(combinedDomain[i])):
                index = combinedDomain[i][j] - 1
                if len(combinedDomain[i]) == 1:
                    occurences[index] += 10
                else:
                    occurences[index] += 1
        # return value and index of cell in the allDiff
        for m in range(len(occurences)):
            if occurences[m] == 1:
                for i in range(self.board_length):
                    for j in range(len(combinedDomain[i])):
                        if combinedDomain[i][j] == m+1:
                            return i, m+1
        return -1, -1

    def checkForNples(self):
        nple = []
        for i in range(self.board_length):
            for j in range(self.board_length):
                allDiff = self.getAllDiffs(i, j) #get allDiffs for every square
                for k in range(self.allDiffsLen):
                    for l in range(self.board_length):
                        nple.append(allDiff[k][l])
                        for m in range(len(allDiff[k])):
                            if (l != m) and (allDiff[k][l].domain == allDiff[k][m].domain):
                                nple.append(allDiff[k][m])
                        if len(nple) > 1 and len(nple) == len(nple[0].domain) :
                            allDiffs.changeDomainofSquares(allDiff[k], allDiff[k][l].domain, nple)
                        nple = []

    def boardChanged(self, board2):
        for x in range(self.board_length):
            for y in range(self.board_length):
                if set(self.board[x][y].domain) != set(board2[x][y].domain):
                    return True
        return False

    def solve(self):
        board2 = copy.deepcopy(self.board)
        print('START')
        self.printBoard()
        self.solveNakedSingles()
        a_iter = 1
        while self.boardChanged(board2):
            board2 = copy.deepcopy(self.board)
            print('SOLUTON #%d' % a_iter)
            self.printBoard()
            self.solveNakedSingles()
            a_iter += 1
        if self.boardIsDone():
            self.printFinalBoard()
        else:
            board2 = copy.deepcopy(self.board)
            self.checkForNples()
            print('After Nples')
            self.printBoard()
            self.solveHiddenSingles()
            print('after hidden singles')
            self.printBoard()
            if self.boardIsDone():
                self.printFinalBoard()
            elif self.boardChanged(board2):
                self.solve()
            else:
                print('FINAL')
                self.printBoard()

    def boardIsDone(self):
        for i in range(self.board_length):
            for j in range(self.board_length):
                if len(self.board[i][j].domain) != 1:
                    return False
        return True

    def printBoard(self):
        for row in range(self.board_length):
            for column in range(self.board_length):
                sys.stdout.write('%20s' % str(self.board[row][column].domain))
            print('')

    def printBoard2(self, board2):
        for row in range(self.board_length):
            for column in range(self.board_length):
                sys.stdout.write('%20s' % str(board2[row][column].domain))
            print('')

    def printFinalBoard(self):
        for row in range(self.board_length):
            for column in range(self.board_length):
                sys.stdout.write('%5s  |' % str(self.board[row][column].domain))
            print('')