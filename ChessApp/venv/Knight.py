from Piece import Piece

class Knight (Piece):

    def __init__(self, color):
        '''
        '''
        self.setName("Knight")
        self.setColor(color)
        self.upAllowed = True
        self.setMoves()

    def __str__ (self):
        return f"{self.getName()}({self.getColor()})"

    def setMoves(self):
        '''
        Updates the movement variables for the knight
        '''
        self.move_set = [[-1,  1, -1,  1, -1], \
                     [1 , -1, -1, -1,  1], \
                     [-1, -1,  0, -1, -1], \
                     [1 , -1, -1, -1,  1], \
                     [-1,  1, -1,  1, -1]]