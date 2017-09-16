class Piece:
    '''
    Superclass for piece type.
    '''

    def __init__(self):
        '''
        Initializes the piece object
        '''
        self.up_allowed = False
        self.left_allowed = False
        self.right_allowed = False
        self.down_allowed = False
        self.diag_left = False
        self.diag_right = False
        self.move_set = [[0, 0, 0],   \
                        [0, 0, 0],   \
                        [0, 0, 0]]

    def getName(self):
        '''
        Returns the name of the piece
        '''
        try:
            return self.name
        except:
            return "N/A"

    def setName(self, name):
        '''
        Gets the name of this piece (e.g. "Rook", "Pawn")
        '''
        self.name = name

    def getColor(self):
        '''
        Returns the color of the piece
        '''
        return self.color

    def setColor(self, color = 0):
        '''
        Sets the color of the piece (0 for white and 1 for black)
        '''
        self.color = color

    def setAllowedMoves(self):
        '''
        Gets the list of squares a piece is allowed to go to relative to itself
        '''
        pass

    def getAllowedMoves(self):
        '''

        '''
        pass

    def getRules(self):
        '''

        '''
        pass