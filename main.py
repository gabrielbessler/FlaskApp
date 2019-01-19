#!/usr/bin/python

''' TEMP '''

import os
import json
import cgitb
import logging
from flask import Flask, request, redirect, abort, render_template
from flask import session
from game import Game

cgitb.enable()

APP = Flask(__name__)
# Generate a random key for user sessions
APP.secret_key = os.urandom(24)

class MetaData():
    ''' Contains all of the metadata about each match'''
    def __init__(self):
        '''
        Sets testing, debug mode, and initializes games
        '''
        # TEST_MODE will disable session checking so that games can be started
        # with 1 user
        self.test_mode = True
        # Debug mode will display useful data
        self.debug_mode = False
        self.num_starting_games = 5

        # 2 for ongoing games, 1 for games with 1 person waiting, 0 otherwise
        self.games = [0] * self.num_starting_games
        self.player_ids = [0]
        self.store_games = {}
        # Store the user IDs for each game
        self.game_players = [[0, 0] for i in range(self.num_starting_games)]

    def is_debug(self):
        ''' Return true if in debug mode '''
        return self.debug_mode

    def get_games(self):
        ''' Get all ongoing games '''
        return self.store_games

MD = MetaData()

@APP.route('/', methods=["POST", "GET"])
def main_page():
    '''
    Handles the main page for the chess web application
    '''
    # If the user requests to join a new game, get the next game available
    # and redirect to URL
    if request.method == "POST":
        next_available_game = get_next_game()
        if next_available_game == -1:
            return json.dumps("error")

        return json.dumps("game\\" + str(next_available_game))

    # Display available games to the user
    # If DEBUG MODE is ON, display the raw data without any styling
    if MD.debug_mode:
        return display_games_available_raw()

    return render_template('index.html', games=MD.games,
                           numberOfGames=len(MD.games))

def display_games_available_raw():
    ''' Displays a list of the games currently available in raw text format
    '''
    display = ""
    for game_index, game_on in enumerate(MD.games):
        display += f"Game {game_index+1}, Available: {bool(not game_on)} <br>"
    return display


def get_next_game():
    '''
    Loops through the list of ongoing games and finds the next game available
    '''
    for game_id, game_value in enumerate(MD.games):
        if game_value < 2:
            return game_id
    return -1


def get_db():
    '''
    Implementing SQL to store usernames and passwords
    '''

@APP.route('/create_game', methods=["POST"])
def create_game():
    '''
    Creates a new empty game that users can join
    '''
    MD.games.append(0)
    MD.game_players.append([0, 0])

@APP.route('/about_us')
def about_us_page():
    '''
    Renders the "About Us" page
    '''
    return render_template('about_us.html')


@APP.route('/get_games', methods=["POST"])
def get_open_games():
    '''
    Gets called every x seconds to check which games are currently open.
    '''
    return json.dumps(MD.games)


@APP.route('/make_move', methods=["POST"])
def get_move():
    ''' Get movedata from AJAX request and make the move for the player
        Request is sent when player clicks on a valid square on the board
    '''
    req_json = request.get_json()
    game_num = req_json[34:]
    move = req_json[0] + req_json[2] + req_json[4] + req_json[6]
    return json.dumps(MD.store_games[int(game_num)].make_move(move))


@APP.route('/get_piece_move', methods=["POST"])
def get_piece_move():
    ''' Runs when the user submits a requests to move a piece.
    Obtains movedata as JSON from AJAX request and makes the corresponding move
    '''
    move_data = request.get_json()
    starting_coord = move_data[0] + move_data[2]
    game_num = move_data[30:]
    allowed_moves = MD.store_games[int(game_num)].get_allowed_moves(starting_coord)
    return json.dumps(allowed_moves)


@APP.route('/ajax', methods=["POST"])
def get_data():
    '''
    Test this
    '''
    try:
        # TODO: test this to make sure it's working with the game number
        request_data = request.get_json()
        print(request_data)
        move_data = request_data # TODO
        return json.dumps(MD.store_games[0].make_move(move_data))
    except KeyError:
        pass


@APP.route('/')
def quick_join():
    '''
    Allows user to join the next available game
    '''
    game_value = get_next_game()
    if game_value == -1:
        return "Games in progress...please wait..."
    return redirect("game\\" + str(get_next_game()))


@APP.route('/show_game', methods=["POST"])
def show_game():
    '''
    Used for spectating a particular game
    '''
    return json.dumps('abc')


@APP.route('/login', methods=["POST"])
def login(data):
    ''' Allows the user to log in '''
    return json.dumps(data)


@APP.route('/spectate/<int:game_num>')
def spectate_game(game_num):
    '''
    Allows the user to spectate a given game
    '''
    print(game_num)
    return render_template("spectate_game.html")


def get_next_id():
    '''
    Gets the next ID not currently begin used
    '''
    MD.player_ids[0] += 1
    return MD.player_ids[0]


@APP.route('/forgot_password')
def forgot_pw():
    '''
    Display page for "forgot password" from login screen
    '''
    return render_template('forgot_password.html')


@APP.route('/game/<int:game_num>', methods=["POST", "GET"])
def get_game(game_num):
    '''
    Handles ongoing chess matches
    '''
    if request.method == "POST":
        try:
            # Use JS to create an AJAX request
            var = request.form['movedata']
            return MD.store_games[game_num].make_move(str(var))
        except KeyError:
            return "Doing a 404<br>Your last move was: " + \
            str(request.form['movedata'])
            # abort(404)

    if request.method == "GET" and game_num < len(MD.games):
        if MD.games[game_num] <= 2:
            if not MD.test_mode:
                if "player_id" in session:
                    # make sure that you are not already in the `
                    if session["player_id"] not in MD.game_players[game_num]:
                        add_new_player(game_num, session["player_id"])
                else:
                    # create a new session for the user
                    session["player_id"] = get_next_id()
                    add_new_player(game_num, session["player_id"])
            else:
                MD.games[game_num] += 1
        if MD.games[game_num] == 2:
            # TODO: check session here?
            new_game = Game()
            MD.store_games[game_num] = new_game

            board_data = MD.store_games[game_num].board.get_raw()
            board_disp = str(MD.store_games[game_num].board)
            return render_template('get_move.html',
                                   board_repr=str(MD.store_games[game_num]),
                                   board_disp=board_disp,
                                   game_num=game_num,
                                   board_data=board_data)
        return render_template('waiting.html', game_num=game_num)

    if request.method == "GET":
        abort(404)

    return None


def add_new_player(game_num, play_id):
    '''
    Checks if the current user is a new player in the game
    '''
    if MD.game_players[game_num][0] == 0:
        MD.game_players[game_num][0] = play_id
    else:
        MD.game_players[game_num][1] = play_id
    MD.games[game_num] += 1


@APP.errorhandler(404)
def page_not_found(err):
    '''
    Actions to take on a 404 error
    '''
    logging.info(err)
    return render_template("404.html")
