"""Sudoku Background

Sudoku is a game played on a 9x9 grid.
The goal of the game is to fill all cells of the grid with digits from 1 to 9,
so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks)
contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)
Sudoku Solution Validator

Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board,
and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's,
which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9."""

def validSolution(board):
    a = 0
    b = 3
    temp = []
    another_temp = []
    patt = list(range(1,10))
    if len(board) != 9 or board.count(0) > 0:
        return False
    else:
        for j in range(3):
            for ind, each in enumerate(board):
                if len(each) != 9 or sorted(each) != patt:
                    return False
                else:
                    for k in range(9):
                        another_temp.append(board[k][ind])
                    else:
                        if sorted(another_temp) != patt:
                            return False
                        else:
                            another_temp.clear()
                    temp += each[a:b]
                    if ind+1 in range(3,10,3):
                        if sorted(temp) != patt:
                            return False
                        temp.clear()
            a += 3
            b += 3
    return True
print(validSolution([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]))