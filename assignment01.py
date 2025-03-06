"""
CS3B, Assignment #1, Tic Tac Toe
Andre Chen
Completed Assignment #1
"""

import time
from enum import Enum, auto

class GameBoardPlayer(Enum):

    
    NONE = 0  #this means either the space on the game board is unoccupied, or there's no winner on the board
    X = 1  #this has value of 1, and means either the space on the game board is occupied by player X, or the winner on the board is player X
    O = 2 #this has value of 2, and means either the space on the game board is occupied by player O, or the winner on the board is player O
    DRAW = 3 #this has value of 3, and means the game is a draw

    def __str__(self): #self refers to each of the numbers of enum, it could be none, x, o , or draw
        if self == GameBoardPlayer.NONE:
            return " "  
        return self.name

        #example: for gameboardplayer.x it returns "x"
        #and for member NONE it should return a single space " "
        
        

    """
    An enum that represents a player on a game board; it's used to denote:
    . which player occupies a space on the board (can be NONE if unoccupied)
    . which player is the winner of the game (can be DRAW)
    """


class ArrayGameBoard:
    """A class that represents a rectangular game board"""

    def __init__(self, nrows, ncols):
        if nrows <= 0 or ncols <= 0:
            raise ValueError("Number of rows and columns must be greater than 0.")
        self.nrows = nrows
        self.ncols = ncols
        self.board = []
        for _ in range(nrows):
            row = [GameBoardPlayer.NONE] * ncols
            self.board.append(row)

    def get_nrows(self):
        return self.nrows

    def get_ncols(self):
        return self.ncols

    def set(self, row, col, value):
        if row < 0 or row >= self.nrows or col < 0 or col >= self.ncols:
            raise IndexError("Row or column index out of bounds.")
        self.board[row][col] = value

    def get(self, row, col):
        if row < 0 or row >= self.nrows or col < 0 or col >= self.ncols:
            raise IndexError("Row or column index out of bounds.")
        return self.board[row][col]

    def __str__(self):
        
        result = ""
        for row in range(self.nrows):
            row_str = ""
            for col in range(self.ncols):
                row_str += str(self.get(row, col))
                if col < self.ncols - 1:
                    row_str += "|"
            result += row_str + "\n"
            #print(result)
        return result   #if you do strip the first board output will be off center



    def get_winner(self):
        nrows, ncols = self.get_nrows(), self.get_ncols()

        # Check rows
        for row in range(nrows):
            if all(self.get(row, col) == self.get(row, 0) != GameBoardPlayer.NONE for col in range(ncols)):
                return self.get(row, 0)

        # Check columns
        for col in range(ncols):
            if all(self.get(row, col) == self.get(0, col) != GameBoardPlayer.NONE for row in range(nrows)):
                return self.get(0, col)

        # Check diagonals (only if square)
        if nrows == ncols:
            # Top-left to bottom-right
            if all(self.get(i, i) == self.get(0, 0) != GameBoardPlayer.NONE for i in range(nrows)):
                return self.get(0, 0)

            # topright to bottomleft
            if all(self.get(i, ncols - 1 - i) == self.get(0, ncols - 1) != GameBoardPlayer.NONE for i in range(nrows)):
                return self.get(0, ncols - 1)

        # Check for a draw
        if all(self.get(row, col) != GameBoardPlayer.NONE for row in range(nrows) for col in range(ncols)):
            return GameBoardPlayer.DRAW

        # No winner yet
        return GameBoardPlayer.NONE


class BitGameBoard:
    """A class that represents a rectangular game board"""

    def __init__(self, nrows, ncols):
        pass

    def get_nrows(self):
        pass

    def get_ncols(self):
        pass

    def set(self, row, col, player):
        pass

    def get(self, row, col):
        pass

    def __str__(self):
        return "(To be implemented)"

    def get_winner(self):
        return GameBoardPlayer.NONE


class TicTacToeBoard:
    """
    A class that represents a Tic Tac Toe game board.
    It's a thin wrapper around the actual game board
    """
    NROWS = 3
    NCOLS = 3

    def __init__(self):
        # The two game boards can be used interchangeably.
        self.board = ArrayGameBoard(self.NROWS, self.NCOLS)
        # self.board = BitGameBoard(self.NROWS, self.NCOLS)

    def set(self, row, col, value):
        if self.board.get(row, col) != GameBoardPlayer.NONE:
            raise ValueError(f"{row} {col} already has {self.board.get(row, col)}")
        self.board.set(row, col, value)

    def clear(self, row, col):
        self.board.set(row, col, GameBoardPlayer.NONE)

    def get(self, row, col):
        return self.board.get(row, col)

    def get_winner(self):
        return self.board.get_winner()

    def __str__(self):
        return self.board.__str__()


# we r tasked to add some more tests in here and add more test () functions for boards of other dimensions 
def test_3x3_game_board(gb):
    # Test __str__()
    print(gb)

    print(f"winner of empty board is '{gb.get_winner()}'")

    gb.set(0, 0, GameBoardPlayer.X)
    gb.set(0, 1, GameBoardPlayer.X)
    gb.set(0, 2, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print("gb.get(0, 1) returns", gb.get(0, 1))
    print("gb.get(0, 2) returns", gb.get(0, 2))

    try:
        gb.get(100, 100)
        print("gb.get(100, 100) fails to raise IndexError")
    except IndexError:
        print("gb.get(100, 100) correctly raises IndexError")

    print(f"winner of board with 1 row of X is '{gb.get_winner()}'")

    # TODO add other tests (GameBoardPlayer.O, different rows, columns, diagonal, etc)

def test_4x4_game_board():
    gb = ArrayGameBoard(4, 4)

    # test __str__()
    print("initial empty 4x4 board:")
    print(gb)

    # valid set and get
    gb.set(3, 3, GameBoardPlayer.X)
    print("set X at (3, 3):")
    print(gb)
    print("get value at (3, 3):", gb.get(3, 3))

    # test for row winner
    gb = ArrayGameBoard(4, 4)
    gb.set(0, 0, GameBoardPlayer.O)
    gb.set(0, 1, GameBoardPlayer.O)
    gb.set(0, 2, GameBoardPlayer.O)
    gb.set(0, 3, GameBoardPlayer.O)
    print("testing get_winner() for a row winner on a 4x4 board:")
    print(gb)
    print("winner:", gb.get_winner())

    # test for column winner
    gb = ArrayGameBoard(4, 4)
    gb.set(0, 2, GameBoardPlayer.X)
    gb.set(1, 2, GameBoardPlayer.X)
    gb.set(2, 2, GameBoardPlayer.X)
    gb.set(3, 2, GameBoardPlayer.X)
    print("testing get_winner() for a column winner on a 4x4 board:")
    print(gb)
    print("winner:", gb.get_winner())

    # test for diagonal winner
    gb = ArrayGameBoard(4, 4)
    gb.set(0, 0, GameBoardPlayer.O)
    gb.set(1, 1, GameBoardPlayer.O)
    gb.set(2, 2, GameBoardPlayer.O)
    gb.set(3, 3, GameBoardPlayer.O)
    print("testing get_winner() for a diagonal winner on a 4x4 board:")
    print(gb)
    print("winner:", gb.get_winner())


if __name__ == '__main__':
    # The same tests should work for both types of *GameBoard
    test_3x3_game_board(ArrayGameBoard(3, 3))
    # test_3x3_game_board(BitGameBoard(3, 3))

    # TODO add tests for boards of other dimensions

