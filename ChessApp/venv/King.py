from Piece import Piece

class King (Piece):

    def __init__(self, color):
        '''
        '''
        self.setName("King")
        self.setColor(color)
        self.upAllowed = True
        self.setMoves()
        self.setValue(10000)

    def __str__(self):
        return f"{self.getName()}({self.getColor()})"

    def setMoves(self):
        '''
        Updates the movement variables for the bishop
        '''
        self.move_set = [[1,1,1], \
                         [1,0,1], \
                         [1,1,1]]