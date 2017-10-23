var canvas = document.querySelector('canvas');
canvas.width = 640;
canvas.height = 640;

var c = canvas.getContext("2d");
var pieces = {};
var board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]];

var startingCoord = [-1,-1];
var endingCoord = [-1,-1];

/*
 *addClickListener()
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
                }
            }
        }
    });
}

/*
 *makeMove(starting, ending)
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
                console.log("true")
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

addClickListener();
loadImages();
makeChessBoard();

/*
 *loadImages()
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

/*
 *draw()
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

/*
 *updateBoard(input)
 */
function updateBoard(input) {
    board = input;
}

/**
 * Draws the chess board
 */
function makeChessBoard() {
    for (var i=0; i<8; i++) {
        for (var j = 0; j < 8; j++) {
            if ((i+j) % 2 == 1) {
                c.fillStyle = "#505050";
            } else {
                c.fillStyle = "#00ff50";
            }
            c.fillRect(i*80, j*80, 80, 80);
        }
    }
}
