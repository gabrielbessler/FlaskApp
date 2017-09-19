from Board import Board

class Game():

    def __init__(self):
        '''
        Creates a new game.
        '''
        self.board = Board()
        self.curr_turn = 0
        self.convertion = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
        self.reverse_convertion = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H"}

    def get_next_move(self):
        return "<form method='POST'> \
                    <input type='text' value='1234' name='movedata'> </input> \
                    <button type='submit'> Make Move! </button> \
                </form>"

    def __repr__(self):
        '''

        '''
        return "This is the representation of the board"

    def __str__(self):
        return "Game Started. <br>"

    def make_move(self, test):
        try:
            return self.board.move([int(test[0]), int(test[1])], [int(test[2]), int(test[3])]) + "<br>" + str(self.board) + "<br><br>" + self.get_next_move()
        except ValueError as err:
            return str(f"{err} <br><br>") + str(self.board) + "<br><br><form method='POST'> \
                    <input type='text' value='1234' name='movedata'> </input> \
                        <button type='submit'> Make Move! </button> \
                </form>"

    #TODO: test
    def convert_notation(self, text, mode="chess"):
        '''
        Input: A string 'text' representing the move we want to make.
            text (coordinate) x1y1x2y2
            text (chess) a4e7
        Output: A string representing the same move but in the other mode.
        '''
        if mode=="chess":
            if text[0] in self.reverse_convertion and text[2] in self.reverse_convertion:
                output_string = self.convertion[text[0]] + text[1] + self.convert_notation[text[2]] + text[3]
            else:
                return "Not a valid moveset"
        elif mode=="coordinates":
            if text[0] in self.convertion and text[2] in self.convertion:
                output_string = self.convertion[text[0]] + text[1] + self.convertion[text[2]] + text[3]
            else:
                return "Not a valid moveset"
        return output_string