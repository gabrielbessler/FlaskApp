from Piece import Piece

class Queen (Piece):

    def __init__(self, color):
        '''
        '''
        self.setName("Queen")
        self.setColor(color)
        self.upAllowed = True
        self.setMoves()

    def __str__(self):
        return f"{self.getName()} {self.getColor()}"

    def setMoves(self):
        '''
        Updates the movement variables for the pawn
        '''
        self.up_allowed = True
        self.diag_left = True
        self.diag_right = True
        self.left_allowed = True
        self.right_allowed = True
        self.down_allowed = True