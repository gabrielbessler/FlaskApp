class Board:
    #Initializes the Board

    def __init__(self):
        self.setInitialState()
        self.board = []
    '''
    takes in two locations. Moves piece from current
    square to next Square and replaces the piece with a zero
    '''

    def move(self, currentSquare, nextSquare):
        '''
        Future implentation
        isValidMove(self, piece, currentSquare, nextSquare)
        '''
        piece = self.board[currentSquare[0], currentSquare[1]]
        self.board[currentSquare[0], currentSquare[1]] = 0
        self.board[nextSquare[0], nextSquare[1]] = piece

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
        return "Gabe Bess"

