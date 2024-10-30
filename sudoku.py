import random

class SudokuGame:
    def __init__(self):
        self.board = [[0 for i in range(9)] for j in range(9)]
    

    def find_empty(self):
        """ Finds an empty cell in the board, returns (row, col) or None if board is full. """
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None
    
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

    def solve_board(self):
        """ Solves the board using backtracking. """
        empty = self.find_empty()

        if empty == None:
            return True
        
        row, col = empty
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        
        for num in numbers:
            if self.is_valid_move(row, col, num):
                self.board[row][col] = num
                if self.solve_board():
                    return True
                self.board[row][col] = 0
        
        return False
    
    def remove_numbers(self, holes=40):
        """ Remove numbers from a solved board to create a puzzle with empty cells. """
        count = 0
        while count < holes:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count+=1
    
    
    def print_board(self):
        print(self.board)

game = SudokuGame()
game.solve_board()
game.print_board()