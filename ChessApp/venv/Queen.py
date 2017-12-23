from Piece import Piece


class Queen (Piece):

    def __init__(self, color):
        '''
        Creates a Queen object of a given color with the allowed
        moveset and value 9
        '''
        self.setName("Queen")
        self.setColor(color)
        self.upAllowed = True
        self.setMoves(upAllowed=True, diagLeft=True, diagRight=True, leftAllowed=True, rightAllowed=True, downAllowed=True)
        self.setValue(9)

    def __str__(self):
        '''
        Returns a string representation of the queen of a given color
        '''
        return f"{self.getName()}({self.getColor()})"
