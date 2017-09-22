from Piece import Piece

class Knight (Piece):

    def __init__(self, color):
        '''
        '''
        self.knightMoves = [[-1,  1, -1,  1, -1], \
                     [1 , -1, -1, -1,  1], \
                     [-1, -1,  0, -1, -1], \
                     [1 , -1, -1, -1,  1], \
                     [-1,  1, -1,  1, -1]]
        self.setName("Knight")
        self.setColor(color)
        self.upAllowed = True
        self.setMoves(moveSet = self.knightMoves)
        self.setValue(3)

    def __str__ (self):
        return f"{self.getName()}({self.getColor()})"
