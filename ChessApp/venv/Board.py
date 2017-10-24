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

    #TODO: fix this
    def getRAW(self):
        stringBoard = '['
        for x in range(8):
            stringBoard += "["
            for y in range(8):
                stringBoard += '"' + str(self.board[x][y]) + '"'
                if y != 7:
                    stringBoard += ','
            stringBoard += "]"
            if x != 7:
                stringBoard += ","
        stringBoard += ']'
        return stringBoard

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

    def move(self, currentSquare, nextSquare, turn):
        '''
        Takes in two locations. Moves piece from current
        square to next Square and replaces the piece with a zero
        '''
        piece = self.board[currentSquare[0]][currentSquare[1]]
        target = self.board[nextSquare[0]][nextSquare[1]]

        #if we try to move an empty square or move a piece no squares, or on top of a piece of our own color
        if piece == 0:
            raise ValueError("No Piece Selected")
        if currentSquare == nextSquare:
            raise ValueError("Cannot Move to Same Position")
        else:
            if target != 0:
                if target.getColor() == piece.getColor():
                    raise ValueError("Cannot Take a Piece of Same Color")
            if piece.getColor() != turn:
                raise ValueError("Cannot move your opponent's piece")
            #check if given a piece and a different starting/ending square, it is a valid move
            if self.isValidMove(piece, currentSquare, nextSquare):
                self.board[currentSquare[0]][currentSquare[1]] = 0
                self.board[nextSquare[0]][nextSquare[1]] = piece
                return f"Made Move: {currentSquare, nextSquare} for piece {piece} <br>"
            else:
                raise ValueError("Move Not in Moveset")

    def check_for_mate(self):
        '''
        TODO
        '''
        # Check if the king is on the board. If not, it is mate
        kingCount = 0
        for row in self.board:
            for col in row:
                if 1 == 1:
                    kingCount += 1
        if kingCount == 2:
            return False
        else:
            return True

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

    def getTotalScore(self):
        '''
        Count the total score for black and white and returns
        [WhiteScore, BlackScore]
        '''
        total_white_score = 0
        total_black_score = 0
        for i in self.board:
            for j in i:
                if j != 0:
                    if j.getColor() == 0:
                        total_white_score += j.getValue()
                    elif j.getColor() == 1:
                        total_black_score += j.getValue()

        return [total_white_score, total_black_score]
