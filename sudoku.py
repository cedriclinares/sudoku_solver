import sys
import cell
import squareBoard

lvl0=[[1,0,7,0,0,0,5,0,0],
      [2,6,0,8,0,0,0,0,3],
      [0,9,5,0,0,1,0,8,0],
      [0,0,2,3,0,8,0,0,0],
      [0,1,0,0,7,0,0,3,0],
      [0,0,0,1,0,4,8,0,0],
      [0,5,0,7,0,0,2,6,0],
      [6,0,0,0,0,2,0,4,1],
      [0,0,9,0,0,0,3,0,8]]

lvl1=[[0,3,0,0,0,0,0,0,0],
      [8,0,9,4,6,0,0,3,0],
      [0,0,0,3,7,0,0,8,4],
      [1,0,0,0,0,3,6,7,9],
      [5,7,0,2,0,0,0,0,8],
      [0,0,8,0,1,6,0,0,5],
      [0,0,0,0,0,5,1,4,0],
      [0,0,0,0,0,2,0,9,0],
      [0,0,1,6,4,0,0,5,0]]

lvl2=[[0,0,4,0,0,6,0,0,0],
      [0,0,0,0,0,3,1,0,0],
      [0,0,6,5,0,0,0,0,0],
      [2,1,0,0,0,5,0,0,8],
      [0,9,0,0,0,0,6,0,0],
      [0,0,0,0,0,0,7,9,0],
      [0,0,8,9,0,2,3,6,0],
      [0,0,0,8,0,0,9,0,0],
      [7,0,0,0,0,0,0,0,2]]


lvl4=[[5,0,0,0,0,7,0,2,4],
      [0,0,1,0,2,0,0,0,5],
      [0,9,7,8,0,0,1,0,0],
      [0,0,3,0,0,0,0,0,7],
      [0,6,0,0,0,0,0,8,0],
      [9,0,0,0,0,0,2,0,0],
      [0,0,9,0,0,6,7,4,0],
      [1,0,0,0,3,0,5,0,0],
      [7,5,0,9,0,0,0,0,2]]

lvl5=[[0,2,0,0,0,0,0,9,0],
      [6,0,0,9,0,5,0,0,4],
      [0,0,1,0,3,0,5,0,0],
      [0,8,0,0,9,0,0,4,0],
      [0,0,3,1,0,8,6,0,0],
      [0,1,0,0,7,0,0,2,0],
      [0,0,2,0,6,0,7,0,0],
      [1,0,0,3,0,2,0,0,8],
      [0,6,0,0,0,0,0,3,0]]

sudoku = squareBoard.squareBoard()
sudoku.getExample(lvl5)
# sudoku.getStartBoard()
# sudoku.printBoard()
#allDiffs = sudoku.getAllDiffs()
#for x in range(len(allDiffs)):
#    for y in range(len(allDiffs[x])):
#        sys.stdout.write(str(allDiffs[x][y].position))
#    print('')
sudoku.solve()