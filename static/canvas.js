/* Creating the canvas and getting the context */
var canvas = document.querySelector('canvas');
canvas.width = 640;
canvas.height = 640;
var c = canvas.getContext("2d");

/* Variables for drawing the chess board */
const SQUARE_WIDTH = 80;
const SQUARE_HEIGHT = 80;
var color1 = "#505050";
var color2 = "#00ff50";


var pieces = {};
var board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]];

var startingCoord = [-1,-1];
var endingCoord = [-1,-1];

addClickListener();
loadImages();
makeChessBoard();

/**
 *
 */
function addClickListener() {

    canvas.addEventListener("click", function() {

        row = Math.floor( (event.pageX-5) / 80);
        col = Math.floor( (event.pageY / 80) ) - 1;

        if (startingCoord[0] != -1 && startingCoord[1] != -1) {
            endingCoord = [row, col];
            makeMove(startingCoord, endingCoord);
        } else {
            if (board[row][col] != 0) {
                if (startingCoord[0] == -1 && startingCoord[1] == -1)
                {
                    startingCoord = [row, col];
                    getMove(startingCoord);
                }
            }
        }
    });
}

/**
 *
 * @param {*} curr_game
 */
function submitMove(curr_game) {
    currMove = document.getElementById("manual_in").value;
    $.ajax({
        type:"POST",
        url:'/ajax',
        dataType: "json",
        contentType: 'application/json; charset=UTF-8',
        data: JSON.stringify({"move": currMove, "gamenum": 0}),
        success: function(data) {
            data = JSON.parse(data);
            document.body.innerHTML = data;
        }
    })
}

/**
 *
 * @param {*} starting
 * @param {*} ending
 */
function makeMove(starting, ending) {
    /* TODO: fix this */
    $.ajax({
        type:'POST',
        url:'/make_move',
        dataType: "json",
        contentType: 'application/json; charset=UTF-8',
        data: JSON.stringify(starting + ',' + ending + window.location),
        success: function(data) {
            if (data == "-1") {
                console.log("INVALID MOVE");
                makeChessBoard();
                draw();
            } else if (data == "1") {
                console.log("YOU LOSE");
            } else {
                updateBoard(JSON.parse(data));
                makeChessBoard()
                draw()
            }
            startingCoord = [-1,-1];
            endingCoord = [-1, -1];
        }
    });
}

/**
 *
 * @param {*} starting
 */
function getMove(starting) {
    $.ajax({
        type:'POST',
        url:'/get_piece_move',
        dataType: "json",
        contentType: 'application/json; charset=UTF-8',
        data: JSON.stringify(starting + window.location),
        success: function(data) {
            if (data.length == 0) {
                startingCoord = [-1, -1]
            }
            for (var i = 0; i < data.length; i++){
                c.strokeStyle = "#ff00ff";
                c.beginPath();
                c.arc(data[i][0]*SQUARE_WIDTH + SQUARE_WIDTH/2, data[i][1]*SQUARE_HEIGHT + SQUARE_HEIGHT/2,20,0,2*Math.PI);
                c.stroke();
            }
        }
    });
}

/**
 *
 */
function loadImages() {
    var imageList = ["/static/bishop_b.png", "/static/bishop_w.png", "/static/king_b.png", "/static/king_w.png", "/static/knight_b.png", "/static/knight_w.png", "/static/pawn_b.png", "/static/pawn_w.png", "/static/queen_b.png", "/static/queen_w.png", "/static/rook_b.png", "/static/rook_w.png"];
    var imageObject;
    count = 0;
    for (var i = 0; i < imageList.length; i++) {
        imageObject = new Image();

        imageObject.onload = function() {
            count++;

            if (count == imageList.length) {
                draw();
            }

        }
        imageObject.src = imageList[i];
        var name =  imageList[i].slice(8,-4);
        var c;
        if (name.charAt(name.length-1) == 'b') {
            var c = "0";
        } else {
            var c = "1";
        }
        pieces[name.charAt(0).toUpperCase() + name.slice(1,-2) + "(" + c + ")"] = imageObject;
    }
}

/**
 *
 */
function draw() {
    for (var row = 0; row < board.length; row++) {
        for (var col = 0; col < board[row]  .length; col++) {
            if (board[row][col] != 0) {
                c.drawImage(pieces[board[row][col]], row*80 + 5, col*80 + 5);
            }
        }
    }
}

/**
 *
 * @param {*} input
 */
function updateBoard(input) {
    board = input;
}

/**
 *
 */
function makeChessBoard() {
    // Loop through the entire board
    for (var i=0; i<board.length; i++) {
        for (var j = 0; j < board[i].length; j++) {
            // Create a checkerboard pattern by alternating colors
            if ((i+j) % 2 == 1) {
                c.fillStyle = color1;
            } else {
                c.fillStyle = color2;
            }
            // Draw a rectangle of the correct width/height
            c.fillRect(i*SQUARE_WIDTH, j*SQUARE_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT);
        }
    }
}
