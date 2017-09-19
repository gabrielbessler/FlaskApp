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
        '''
        Returns a string representation of the current board
        '''
        stringBoard = ''
        for x in range(8):
            for y in range(8):
                stringBoard += str(self.board[x][y]) + ' '
            stringBoard += '<br>'
        return stringBoard

    def move(self, currentSquare, nextSquare):
        '''
        Takes in two locations. Moves piece from current
        square to next Square and replaces the piece with a zero
        '''
        piece = self.board[currentSquare[0]][currentSquare[1]]
        target = self.board[currentSquare[0]][currentSquare[1]]
        #if we try to move an empty square or move a piece no squares, or on top of a piece of our own color
        if piece == 0 or currentSquare == nextSquare or target.getColor() == piece.getColor():
            raise ValueError
        else:
            #check if given a piece and a different starting/ending square, it is valid
            if self.isValidMove(piece, currentSquare, nextSquare):
                self.board[currentSquare[0]][currentSquare[1]] = 0
                self.board[nextSquare[0]][nextSquare[1]] = piece
                return f"Made Move: {currentSquare, nextSquare} for piece {piece} <br>"
            else:
                raise ValueError

    def isValidMove(self, piece, currentSquare, nextSquare):
        '''TODO'''
        #first, we get the allowed moveset from the piece
        allowed_moves = piece.getAllowedMoves()
        #then, we check the difference between the nextSquare and currentSquare
        x_diff = nextSquare[0] - currentSquare[0]
        y_diff = nextSquare[1] - currentSquare[1]
        return True

    def checkWinner(self):
        '''
        Checks winner by determining if there are two kings on the
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


    def getBoard(self):
        '''
        Returns the current board
        '''
        return self.board

    def setInitialState(self):
        '''
        Creates and initializes the board
        '''
        self.board = [[Rook(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Rook(0)],
                      [Knight(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Knight(0)],
                      [Bishop(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Bishop(0)],
                      [Queen(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Queen(0)],
                      [King(1), Pawn(1), 0, 0, 0, 0, Pawn(0), King(0)],
                      [Bishop(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Bishop(0)],
                      [Knight(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Knight(0)],
                      [Rook(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Rook(0)]]

