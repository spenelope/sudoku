import time
import numpy as np

#puzzle
puzzle = [[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]]


order = (3,3)

class sudoku:
    solutions = 0

    def print_array(array, order):   #board
        a, b, c = order[0] * order[1], order[0], order[1]
        for x in range(a):
                for y in range(a):
                    if (y + 1) % c == 0 and y+1 != a:
                        print(f"{array[x][y]:3d}", end=" |")
                    else:
                        print(f"{array[x][y]:3d}", end="")
                print()
                if (x + 1) % b == 0 and (x+1) != a:
                    print("-" * ((0 * order[0] * order[1]) + order[0] * 0 ))
        print()

   

sudoku.print_array(puzzle, order)
