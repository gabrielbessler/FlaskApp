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
        self.move_set = [[0, 0, 0],
                         [0, 0, 0],
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

    def setColor(self, color=0):
        '''
        Sets the color of the piece (0 for white and 1 for black)
        '''
        self.color = color

    def setMoves(self, upAllowed=False, leftAllowed=False, rightAllowed=False,
                 downAllowed=False, diagLeft=False, diagRight=False,
                 moveSet=[]):
        '''
        Gets the list of squares a piece is allowed to go to relative to itself
        '''
        self.up_allowed = upAllowed
        self.left_allowed = leftAllowed
        self.right_allowed = rightAllowed
        self.down_allowed = downAllowed
        self.diag_left = diagLeft
        self.diag_right = diagRight
        self.move_set = moveSet

    def getAllowedMoves(self):
        '''
        Returns a list of the moves a particular piece is allowed to make
        '''
        return [self.up_allowed, self.left_allowed, self.right_allowed,
                self.down_allowed, self.diag_left, self.diag_right,
                self.move_set]

    def setValue(self, value):
        '''
        Sets the centipawn value of a piece (1 represents 100 centipawns)
        '''
        self.value = value

    def getValue(self):
        '''
        Returns the centipawn value of a given piece
        (1 represents 100 centipawns)
        '''
        return self.value