import random
import copy

class SudokuGame:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.generate_board()
        

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

    def make_move(self, row, col, num):
        if self.board[row][col] == 0 and self.is_valid_move(row, col, num):
            self.board[row][col] = num
            return True
        return False

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
    
    def remove_numbers(self, holes=45):
        """ Remove numbers from a solved board to create a puzzle with 
        empty cells bounded by the input [holes] """
        count = 0
        while count < holes:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count+=1

    def generate_board(self):
        """Generates a random sudoku board for playing"""
        self.solve_board()
        self.remove_numbers()

    def full(self):
        """Determines if the board is full or not"""
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
        
        return True
    
    def print_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            row = ""
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    row += " | "
                row += f"{self.board[i][j] if self.board[i][j] != 0 else '.'} "
            print(row)
        print()

    def play(self):
        print("Welcome to Sudoku!")
        while self.full() != True:
            self.print_board()
            solution = input("Enter anything to continue or 'give up' to get solution: ")
            if solution == "give up":
                self.solve_board()
                print("Here is your solution: ")
                self.print_board()
                return
            try:
                row = int(input("Enter row (1-9): ")) - 1
                col = int(input("Enter column (1-9): ")) - 1
                num = int(input("Enter number (1-9): "))

                if row < 0 or row > 8 or col < 0 or col > 8 or num < 1 or num > 9:
                    print("Invalid input. Out of Range.")
                    continue

                if self.make_move(row, col, num):
                    print("Move accepted.")
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter a number.")

        print("You've completed the Sudoku puzzle.")
        self.print_board()

game = SudokuGame()
game.play()