from Rook import Rook
from Pawn import Pawn
from King import King
from Queen import Queen
from Bishop import Bishop
from Knight import Knight


class Board:
    def __init__(self):
        '''
        Sets up all of the pieces that are initially on the board
        when the game starts
        '''
        self.board = []
        self.setInitialState()

    def getRAW(self):
        ''' Get the raw data from the board to send to the user
        '''
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
        Used for debugging
        '''
        stringBoard = ''
        for x in range(8):
            for y in range(8):
                stringBoard += str(self.board[x][y]) + ' '
            stringBoard += '<br>'
        return stringBoard

    def getMove(self, coord, turn=-1):
        '''
        Gets all of the available squares that the piece at the given input
        coordinate can move to.
        '''
        # How we store the squares the piece can move to
        allowedSquares = []
        # First, we get the piece on the current board
        piece = self.board[int(coord[0])][int(coord[1])]

        # Make sure the player is not trying to move a piece of the wrong color
        if turn != -1:
            if piece.getColor() != turn:
                return []

        # Obtain the moveset for the given piece
        allowed_moves = piece.getAllowedMoves()
        # Then, compute the allowed coordinates
        for index, val in enumerate(allowed_moves):

            if index == len(allowed_moves) - 1:
                center = [0, 0]
                L = []
                coordX = int(coord[0])
                coordY = int(coord[1])

                for rownum, row in enumerate(val):
                    for colnum in range(len(row)):
                        if val[rownum][colnum] == 0:
                            center = [rownum, colnum]

                centerX = center[1]
                centerY = center[0]

                for rownum, row in enumerate(val):
                    for colnum in range(len(row)):
                        if val[rownum][colnum] == 1:
                            L += [[colnum-centerX+coordX,
                                  rownum-centerY+coordY]]
                        elif val[rownum][colnum] == 3:
                            if not piece.hasMoved:
                                L += [[colnum-centerX+coordX,
                                      rownum-centerY+coordY]]
                        elif val[rownum][colnum] == 2:
                            pos1 = colnum-centerX+coordX
                            pos2 = rownum-centerY+coordY
                            piece2 = self.board[pos1][pos2]
                            if piece2 != 0:
                                if piece2.getColor() != int(turn):
                                    L += [[colnum-centerX+coordX,
                                          rownum-centerY+coordY]]

                allowedSquares += self.checkPieces(L, turn)

            else:
                if val:
                    coordX = int(coord[0])
                    coordY = int(coord[1])
                    # up_allowed
                    if index == 0:
                        L = []
                        for x in range(coordY+1, 8):
                            if x != coordY:
                                piece = self.board[coordX][x]
                        L = self.checkPieces(L, turn)
                        allowedSquares += L
                    # left_allowed
                    elif index == 1:
                        L = [[x, coordY] for x in range(8) if x != coordX]
                        L = self.checkPieces(L, turn)
                        allowedSquares += L
                    # right_allowed
                    elif index == 2:
                        pass
                    # down_allowed
                    elif index == 3:
                        L = []
                        for x in range(0, coordY):
                            if x != coordY:
                                L.append([coordX, x])
                        L = self.checkPieces(L, turn)
                        allowedSquares += L
                    elif index == 4:  # diag_left
                        L = [[coordX-1-x, coordY-1-x] for x in
                             range(min(coordX, coordY))]
                        L2 = [[coordX+1+x, coordY+1+x] for x in
                              range(min(7-coordX, 7-coordY))]
                        L = self.checkPieces(L, turn)
                        L2 = self.checkPieces(L2, turn)
                        allowedSquares += L2
                        allowedSquares += L
                    elif index == 5:  # diag_right
                        L = [[coordX-1-x, coordY+1+x] for x in range(coordX)]
                        L2 = [[coordX+1+x, coordY-1-x] for x in
                              range(7-coordX)]
                        L2 = self.checkPieces(L2, turn)
                        L = self.checkPieces(L, turn)
                        allowedSquares += L2
                        allowedSquares += L
        return allowedSquares

    def isPiece(self, coord):
        '''
        TODO: use this
        '''
        piece = self.board[coord[0]][coord[1]]
        if piece == 0:
            return False
        return True

    def checkPieces(self, L, turn):
        '''
        Given a set of available moves, removes all of the pieces that are of
        the same color as your piece
        '''
        outL = []
        for coord in L:
            try:
                piece = self.board[coord[0]][coord[1]]
                if piece == 0:
                    outL.append(coord)
                else:
                    if piece.getColor() != int(turn):
                        outL.append(coord)
                    else:
                        pass
            except:
                pass

        return outL

    def move(self, currentSquare, nextSquare, turn):
        '''
        Takes in two locations. Moves piece from current
        square to next Square and replaces the piece with a zero
        '''
        piece = self.board[currentSquare[0]][currentSquare[1]]
        target = self.board[nextSquare[0]][nextSquare[1]]

        # if we try to move an empty square or move a piece no squares,
        #  or on top of a piece of our own color
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
            # check if given a piece and a different starting/ending square,
            # it is a valid move
            if self.isValidMove(piece, currentSquare, nextSquare):
                self.board[currentSquare[0]][currentSquare[1]] = 0
                self.board[nextSquare[0]][nextSquare[1]] = piece
                if hasattr(piece, 'hasMoved'):
                    piece.hasMoved = True
                return f"Made Move: {currentSquare, nextSquare} \
                for piece {piece} <br>"
            else:
                raise ValueError("Move Not in Moveset")

    def check_for_mate(self):
        ''' Looks at the current board state and returns True if there
        is a checkmate
        '''

        # TODO: First, check if the king is in check
        # If the king is in check, check if it has any available moves

        # Check if the king is on the board. If not, it is mate
        kingCount = 0
        for row in self.board:
            for col in row:
                if 1 == 1:
                    kingCount += 1
        if kingCount == 2:
            return True
        else:
            return False

    def isValidMove(self, piece, currentSquare, nextSquare):
        '''
        TODO
        '''
        moveL = self.getMove(currentSquare)
        if nextSquare in moveL:
            return True
        return False

        # then, we check the difference between the nextSquare and
        # currentSquare
        # x_diff = nextSquare[0] - currentSquare[0]
        # y_diff = nextSquare[1] - currentSquare[1]

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
