from Board import Board

class Game():

    def __init__(self):
        '''

        '''
        self.board = Board()
        self.curr_turn = 0

    def __repr__(self):
        '''

        '''
        return "This is the representation of the board"