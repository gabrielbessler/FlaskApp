from flask import Flask, request, redirect, abort, render_template, jsonify
from Game import Game
import json
app = Flask(__name__)

# 2 for ongoing games
# 1 for games with 1 person waiting
# 0 otherwise
games = [0] * 10
store_games = {}

@app.route('/', methods=["POST", "GET"])
def main_page():
    '''
    Handles the main page for the chess web application
    '''
    # If the user requests to join a new game, get the next game available and redirect to URL
    if request.method == "POST":
        game_value = get_next_game()
        if game_value == -1:
            return "Games in progress...please wait..."
        else:
            return redirect("game\\" + str(get_next_game()))

    # Display available games to the user
    display = ""
    for game_index, game_on in enumerate(games):
        display += f"Game {game_index+1}, Available: {bool(not game_on)} <br>"

    return render_template('index.html', games = games)
    #return display + render_template('index.html')

def get_next_game():
    '''
    Loops through the list of ongoing games and finds the next game available
    '''
    for game_id, game_value in enumerate(games):
        if game_value < 2:
            return game_id
    return -1

@app.route('/about_us')
def about_us_page():
    return "Work in Progress"

@app.route('/get_games', methods=["GET"])
def get_open_games():
    '''
    Gets called every 'x' seconds to check which games are currently open.
    '''
    return json.dumps(games)

@app.route('/ajax', methods=["POST", "GET"])
def get_data():
    data_here = ['1', '2', '3']
    return json.dumps(data_here)

@app.route('/quick_join')
def quick_join():
    game_value = get_next_game()
    if game_value == -1:
        return "Games in progress...please wait..."
    else:
        return redirect("game\\" + str(get_next_game()))

@app.route('/game/<int:game_num>', methods=["POST", "GET"])
def get_game(game_num):
    '''
    Handles ongoing chess matches
    '''
    if request.method == "POST":
        try:
            # here, we want to use JS to create an AJAX request
            var = request.form['movedata']
            return store_games[game_num].make_move(str(var))
        except (KeyError):
            return "Doing a 404<br>Your last move was: " + str(request.form['movedata'])
            abort(404)
    elif request.method == "GET":
        if games[game_num] <= 2:
            games[game_num] += 1
            if games[game_num] == 2:
                new_game = Game()
                store_games[game_num] = new_game
                return str(store_games[game_num]) + "<br>" + str(store_games[game_num].board) + "<br>" + render_template('get_move.html')
        return f'This is game number {game_num}'

@app.route('/temp')
def page_not_found():
    '''
    Actions to take on a 404 error.
    '''
    pass