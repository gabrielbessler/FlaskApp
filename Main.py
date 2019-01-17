#!/usr/bin/python

from flask import Flask, request, redirect, abort, render_template, jsonify
from flask import session, g
from Game import Game
import json
import os
import cgitb
import sqlite3
import time

cgitb.enable()

app = Flask(__name__)
# Generate a random key for user sessions
app.secret_key = os.urandom(24)

# TEST_MODE will disable session checking so that games can be started
#  with 1 user
TEST_MODE = True
# Debug mode will display useful data
DEBUG_MODE = False
NUM_STARTING_GAMES = 5

# 2 for ongoing games, 1 for games with 1 person waiting, 0 otherwise
games = [0] * NUM_STARTING_GAMES
# Store the user IDs for each game
game_players = [[0, 0] for i in range(NUM_STARTING_GAMES)]
store_games = {}
player_ids = [0]


@app.route('/', methods=["POST", "GET"])
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
        else:
            return json.dumps("game\\" + str(next_available_game))

    # Display available games to the user
    # If DEBUG MODE is ON, display the raw data without any styling
    if DEBUG_MODE:
        return display_games_available_RAW()
    else:
        return render_template('index.html', games=games,
                               numberOfGames=len(games))


def display_games_available_RAW():
    ''' Displays a list of the games currently available in raw text format
    '''
    display = ""
    for game_index, game_on in enumerate(games):
        display += f"Game {game_index+1}, Available: {bool(not game_on)} <br>"
    return display


def get_next_game():
    '''
    Loops through the list of ongoing games and finds the next game available
    '''
    for game_id, game_value in enumerate(games):
        if game_value < 2:
            return game_id
    return -1


def get_db():
    '''
    Implementing SQL to store usernames and passwords
    '''
    pass


@app.route('/create_game', methods=["POST"])
def create_game():
    '''
    Creates a new empty game that users can join
    '''
    try:
        games.append(0)
        game_players.append([0, 0])
        return "success"
    except:
        return "error"


@app.route('/about_us')
def about_us_page():
    '''
    Renders the "About Us" page
    '''
    return render_template('about_us.html')


@app.route('/get_games', methods=["POST"])
def get_open_games():
    '''
    Gets called every x seconds to check which games are currently open.
    '''
    return json.dumps(games)


@app.route('/make_move', methods=["POST"])
def get_move():
    ''' Get movedata from AJAX request and make the move for the player
        Request is sent when player clicks on a valid square on the board
    '''
    a = request.get_json()
    game_num = a[34:]
    move = a[0] + a[2] + a[4] + a[6]
    return json.dumps(store_games[int(game_num)].make_move(move))


@app.route('/get_piece_move', methods=["POST"])
def get_piece_move():
    ''' Runs when the user submits a requests to move a piece.
    Obtains movedata as JSON from AJAX request and makes the corresponding move
    '''
    move_data = request.get_json()
    startingCoord = move_data[0] + move_data[2]
    gameNum = move_data[30:]
    allowedMoves = store_games[int(gameNum)].getAllowedMoves(startingCoord)
    return json.dumps(allowedMoves)


@app.route('/ajax', methods=["POST"])
def get_data():
    '''
    '''
    try:
        # TODO: test this to make sure it's working with the game number
        request_data = request.get_json()
        print(request_data)
        return json.dumps(store_games[0].make_move(move_data))
    except (KeyError):
        pass


@app.route('/')
def quick_join():
    '''
    Allows user to join the next available game
    '''
    game_value = get_next_game()
    if game_value == -1:
        return "Games in progress...please wait..."
    else:
        return redirect("game\\" + str(get_next_game()))


@app.route('/show_game', methods=["POST"])
def show_game():
    '''
    Used for spectating a particular game
    '''
    return json.dump('abc')


@app.route('/login', methods=["POST"])
def login(data):
    return json.dumps(data)


@app.route('/spectate/<int:game_num>')
def spectate_game(game_num):
    '''
    Allows the user to spectate a given game
    '''
    return render_template("spectate_game.html")


def get_next_id():
    '''
    Gets the next ID not currently begin used
    '''
    player_ids[0] += 1
    return player_ids[0]


@app.route('/forgot_password')
def forgot_pw():
    '''
    Display page for "forgot password" from login screen
    '''
    return render_template('forgot_password.html')


@app.route('/game/<int:game_num>', methods=["POST", "GET"])
def get_game(game_num):
    '''
    Handles ongoing chess matches
    '''
    if request.method == "POST":
        try:
            # Use JS to create an AJAX request
            var = request.form['movedata']
            return store_games[game_num].make_move(str(var))
        except (KeyError):
            return "Doing a 404<br>Your last move was: " +
            str(request.form['movedata'])
            abort(404)
    elif request.method == "GET":
        if game_num < len(games):
            if games[game_num] <= 2:
                if not TEST_MODE:
                    if "player_id" in session:
                        # make sure that you are not already in the `
                        if session["player_id"] not in game_players[game_num]:
                            addNewPlayer(game_num, session["player_id"])
                    else:
                        # create a new session for the user
                        session["player_id"] = get_next_id()
                        addNewPlayer(game_num, session["player_id"])
                else:
                    games[game_num] += 1
            if games[game_num] == 2:
                # TODO: check session here?
                new_game = Game()
                store_games[game_num] = new_game

                board_data = store_games[game_num].board.getRAW()
                board_disp = str(store_games[game_num].board)
                return render_template('get_move.html',
                                       board_repr=str(store_games[game_num]),
                                       board_disp=board_disp,
                                       game_num=game_num,
                                       board_data=board_data)
            else:
                return render_template('waiting.html', game_num=game_num)
        else:
            abort(404)


def addNewPlayer(game_num, play_id):
    '''
    Checks if the current user is a new player in the game
    '''
    if game_players[game_num][0] == 0:
        game_players[game_num][0] = play_id
    else:
        game_players[game_num][1] = play_id
    games[game_num] += 1


@app.errorhandler(404)
def page_not_found(e):
    '''
    Actions to take on a 404 error
    '''
    return render_template("404.html")
