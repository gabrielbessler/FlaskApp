from Rook import Rook
from Pawn import Pawn
from King import King
from Queen import Queen
from Bishop import Bishop
from Knight import Knight

class Board:
    #Initializes the Board

    def __init__(self):
        self.board = []
        self.setInitialState()

    '''
    takes in two locations. Moves piece from current
    square to next Square and replaces the piece with a zero
    '''

    def move(self, currentSquare, nextSquare):
        '''
        Future implentation
        isValidMove(self, piece, currentSquare, nextSquare)
        '''
        piece = self.board[currentSquare[0]][currentSquare[1]]
        self.board[currentSquare[0]][currentSquare[1]] = 0
        self.board[nextSquare[0]][nextSquare[1]] = piece
        return str(self.board) + "<form method='POST'> \
                    <input type='text' value='1234' name='test'> </input> \
                    <button type='submit'> Make Move! </button> \
            </form>"
    '''
    checks winner by determining if there are two kings on the
    board
    '''
    def checkWinner(self):
        return "white"

    '''
    returns the current board
    '''
    def getBoard(self):
        return self.board

    '''
    creates and initializes the board
    '''
    def setInitialState(self):
        self.board = [[Rook(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Rook(0)],
                      [Knight(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Knight(0)],
                      [Bishop(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Bishop(0)],
                      [Queen(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Queen(0)],
                      [King(1), Pawn(1), 0, 0, 0, 0, Pawn(0), King(0)],
                      [Bishop(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Bishop(0)],
                      [Knight(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Knight(0)],
                      [Rook(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Rook(0)]]

