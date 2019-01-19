'''
Contains all of the different pieces in the game
as well as a base 'Piece' class
'''

class Piece:
    '''
    Superclass for piece type.
    '''

    # pylint: disable=too-many-instance-attributes

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
        self.name = None
        self.color = None
        self.value = None

    def get_name(self):
        '''
        Returns the name of the piece
        '''
        return self.name

    def set_name(self, name):
        '''
        Gets the name of this piece (e.g. "Rook", "Pawn")
        '''
        self.name = name

    def get_color(self):
        '''
        Returns the color of the piece
        '''
        return self.color

    def set_color(self, color=0):
        '''
        Sets the color of the piece (0 for white and 1 for black)
        '''
        self.color = color

    def set_moves_horiz(self, upallowed=False, leftallowed=False,
                        rightallowed=False, downallowed=False):
        ''' Sets where a piece is able to move relative to itself'''
        self.up_allowed = upallowed
        self.left_allowed = leftallowed
        self.right_allowed = rightallowed
        self.down_allowed = downallowed

    def set_moves_diag(self, diagleft=False, diagright=False):
        ''' Sets where a piece is able to move relative to itself '''
        self.diag_left = diagleft
        self.diag_right = diagright

    def set_moves(self, moveset=None):
        '''
        Gets the list of squares a piece is allowed to go to relative to itself
        '''
        if moveset is None:
            self.move_set = []

    def get_allowed_moves(self):
        '''
        Returns a list of the moves a particular piece is allowed to make
        '''
        return [self.up_allowed, self.left_allowed, self.right_allowed,
                self.down_allowed, self.diag_left, self.diag_right,
                self.move_set]

    def set_value(self, value):
        '''
        Sets the centipawn value of a piece (1 represents 100 centipawns)
        '''
        self.value = value

    def get_value(self):
        '''
        Returns the centipawn value of a given piece
        (1 represents 100 centipawns)
        '''
        return self.value

class Rook(Piece):
    ''' Rook Piece '''
    def __init__(self, color):
        '''
        Creates a rook object of a given color with the allowed
        moveset and value 5
        '''
        super(Rook, self).__init__()

        self.set_name("Rook")
        self.set_color(color)
        self.up_allowed = True
        self.set_moves_horiz(leftallowed=True, rightallowed=True, upallowed=True, downallowed=True)
        self.set_value(5)

    def __str__(self):
        '''
        Returns the String representation of the Rook
        '''
        return f"{self.get_name()}({self.get_color()})"

class Queen(Piece):
    '''
    Queen Piece
    '''
    def __init__(self, color):
        '''
        Creates a Queen object of a given color with the allowed
        moveset and value 9
        '''
        super(Queen, self).__init__()

        self.set_name("Queen")
        self.set_color(color)
        self.up_allowed = True
        self.set_moves_horiz(upallowed=True, leftallowed=True, rightallowed=True, downallowed=True)
        self.set_moves_diag(diagleft=True, diagright=True)
        self.set_value(9)

    def __str__(self):
        '''
        Returns a string representation of the queen of a given color
        '''
        return f"{self.get_name()}({self.get_color()})"
class Pawn(Piece):
    ''' Pawn Piece '''
    def __init__(self, color):
        '''
        Creates a Queen object of a given color with the allowed
        moveset and value 1
        '''
        super(Pawn, self).__init__()

        self.set_name("Pawn")
        self.set_color(color)
        self.up_allowed = True
        if color == 0:
            self.set_moves(moveset=[[-1, 3, -1], [2, 1, 2], [-1, 0, -1]])
        else:
            self.set_moves(moveset=[[-1, 0, -1], [2, 1, 2], [-1, 3, -1]])
        self.set_value(1)
        self.has_moved = False

    def __str__(self):
        '''
        Returns a string representation of the pawn of a given color
        '''
        return f"{self.get_name()}({self.get_color()})"

class Knight(Piece):
    ''' Knight Piece '''
    def __init__(self, color):
        '''
        Creates a Knight object of a given color with the allowed moveset
        and value 3
        '''
        super(Knight, self).__init__()

        self.knight_moves = [[-1, 1, -1, 1, -1],
                             [1, -1, -1, -1, 1],
                             [-1, -1, 0, -1, -1],
                             [1, -1, -1, -1, 1],
                             [-1, 1, -1, 1, -1]]
        self.set_name("Knight")
        self.set_color(color)
        self.up_allowed = True
        self.set_moves(moveset=self.knight_moves)
        self.set_value(3)

    def __str__(self):
        '''
        Returns a string representation of a knight of a given color
        '''
        return f"{self.get_name()}({self.get_color()})"

class King(Piece):
    ''' King Piece '''
    def __init__(self, color):
        '''
        Creates a King object of a given color with the allowed moveset
        and value 0
        '''
        super(King, self).__init__()

        self.king_moves = [[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]]
        self.set_name("King")
        self.set_color(color)
        self.up_allowed = True
        self.set_moves(moveset=self.king_moves)
        self.set_value(0)

    def __str__(self):
        '''
        Returns a string representation of a King of a given color
        '''
        return f"{self.get_name()}({self.get_color()})"

class Bishop(Piece):
    ''' Bishop Piece '''
    def __init__(self, color):
        '''
        Creates a Bishop object of a given color with the allowed moveset
        and value 4
        '''
        super(Bishop, self).__init__()

        self.set_name("Bishop")
        self.set_color(color)
        self.up_allowed = True
        self.set_moves_diag(diagright=True, diagleft=True)
        self.set_value(3)

    def __str__(self):
        '''
        Returns a string representation of a King of a given color
        '''
        return f"{self.get_name()}({self.get_color()})"
