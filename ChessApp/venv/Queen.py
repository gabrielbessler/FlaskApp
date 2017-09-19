from Piece import Piece

class Queen (Piece):

    def __init__(self, color):
        '''
        '''
        self.setName("Queen")
        self.setColor(color)
        self.upAllowed = True
        self.setMoves(upAllowed = True, diagLeft = True, diagRight = True, leftAllowed = True, rightAllowed = True, downAllowed = True)

    def __str__(self):
        return f"{self.getName()}({self.getColor()})"