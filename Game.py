from Board import Board
from flask import render_template
import random
import math

DEBUG_MODE = False


class Game():

    def __init__(self, ai_mode=False):
        '''
        Creates a new game.
        '''
        self.board = Board()
        self.curr_turn = 1  # white
        self.convertion = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
                           "G": 7, "H": 8}
        self.reverse_convertion = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E",
                                   6: "F", 7: "G", 8: "H"}

        self.ai_mode = ai_mode
        if (self.ai_mode):
            start_ai()

    def start_ai(self):
        '''
        '''
        num = random.randint(0, 1)
        self.engine = AI(num, 5)

    def getAllowedMoves(self, coord):
        '''
        Returns a list representing the set of allowed moves for the piece at
         a given coordinate
        '''
        return self.board.getMove(coord, self.curr_turn)

    def make_move(self, coord):
        '''
        Given a String the form 'abcd' where
        (a,b) is the starting coordinate and
        (c,d) is the ending coordinate,

        Make a move in the board if the move is valid.
        '''
        # TODO: fix
        try:
            move_in1 = [int(coord[0]), int(coord[1])]
            move_in2 = [int(coord[2]), int(coord[3])]
            self.board.move(move_in1, move_in2, self.curr_turn)

            if self.curr_turn == 0:
                self.curr_turn = 1
            else:
                self.curr_turn = 0

            isMate = self.board.check_for_mate()

            if isMate:
                return 1
            return self.board.getRAW()
        except ValueError as err:
            if DEBUG_MODE:
                return str(f"{err} <br><br>") + str(self.board) + "<br><br>" +
                render_template("get_move.html")
            return -1

        # OLD CODE
        try:
            get_score = self.board.getTotalScore()
            display_score = f"White: {get_score[0]} points. Black: \
            {get_score[1]} points."
            move_in1 = [int(test[0]), int(test[1])]
            move_in2 = [int(test[2]), int(test[3])]
            rt_str = self.board.move(move_in1, move_in2, self.curr_turn) + \
                "<br>Current Move:" + str(self.curr_turn) + "<br>" +  \
                display_score + "<br><br>" + str(self.board) + \
                render_template('display_board.html',
                                board=self.board.board) + \
                "<br><br>" + render_template("get_move.html")
            if self.curr_turn == 0:
                self.curr_turn = 1
            else:
                self.curr_turn = 0
            return rt_str
        except ValueError as err:
            return str(f"{err} <br><br>") + str(self.board) + "<br><br>" +
            render_template("get_move.html")

    def convert_notation(self, text, mode="chess"):
        '''
        Input: A string 'text' representing the move we want to make.
            text (coordinate) x1y1x2y2
            text (chess) a4e7
        Output: A string representing the same move but in the other mode.
        '''
        if mode == "chess":
            if text[0] in self.reverse_convertion and \
               text[2] in self.reverse_convertion:
                output_string = self.convertion[text[0]] + text[1] + \
                                self.convert_notation[text[2]] + text[3]
            else:
                return "Not a valid moveset"
        elif mode == "coordinates":
            if text[0] in self.convertion and text[2] in self.convertion:
                output_string = self.convertion[text[0]] + text[1] + \
                                self.convertion[text[2]] + text[3]
            else:
                return "Not a valid moveset"
        return output_string
