import random

class SudokuGame:
    def __init__(self):
        self.board = [[0 for i in range(9)] for j in range(9)]
    
    def is_valid_move(self, row, col, num):
        """ Check if a number can be placed at (row, col) without violating Sudoku rules. """
        
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False

        return True
    
    def print_board(self):
        print(self.board)

game = SudokuGame()
game.print_board()