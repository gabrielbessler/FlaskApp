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

    def __str__(self):
        stringBoard = ''
        for x in range(8):
            for y in range(8):
                stringBoard += str(self.board[x][y]) + ' '
            stringBoard += '<br>'
        return stringBoard
    '''
    takes in two locations. Moves piece from current
    square to next Square and replaces the piece with a zero
    '''

    def move(self, currentSquare, nextSquare):
        piece = self.board[currentSquare[0]][currentSquare[1]]
        if piece == 0:
            raise KeyError
        else:
            if self.isValidMove(piece, currentSquare, nextSquare):
                self.board[currentSquare[0]][currentSquare[1]] = 0
                self.board[nextSquare[0]][nextSquare[1]] = piece
                return f"Made Move: {currentSquare, nextSquare} for piece {piece} <br>"
            else:
                raise KeyError

    def isValidMove(self, piece, currentSquare, nextSquare):
        '''TODO'''
        return True


    def checkWinner(self):
        '''
        checks winner by determining if there are two kings on the
        board
        '''
        kingList = []
        for col in self.board:
            for row in self.board:
                if str(row) == "King":
                    kingList.append(row)
        if length(kingList) == 1:
            return kingList[0].getColor()
        pass

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

