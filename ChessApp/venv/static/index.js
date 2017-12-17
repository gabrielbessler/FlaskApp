gameCreatedCount = 0;

    /**
     *
     */
    function createNewGameAlert() {
        $('#gameCreatedAlert').fadeIn('slow');
        gameCreatedCount++;
        if (gameCreatedCount > 1) {
            document.getElementById("gameCreatedAlert").innerHTML("New Game Created (" + gameCreatedCount +")");
        }
    }

    /**
     *
     */
    function createErrorAlert(errorString) {
        $('#errorAlert').fadeIn('slow');
    }

    /**
     *
     */
    function createNoGamesAlert() {
        $('#alert').fadeIn('slow');
    }

    /**
     *
    */
    setInterval(function() {
        $.ajax({
            type: "POST",
            url: '/get_games',
            success: function(data) {
                data = JSON.parse(data);
                // data.length to display all, but will cause error since we only
                // have numGame slots available
                for (var i=0; i < document.getElementById("numGames").getAttribute('data'); i++){
                    try {
                        el = document.getElementById(i);
                        el.innerHTML = "Game Number: " + i + ", Number of Players: " + data[i];
                        if (data[i] == 0) {
                            el.style.color = "green";
                            el.innerHTML += "<input gameval='" + i + "'type='button' class='btn btn-success pull-right' value='Join Game'></input>";
                        } else if(data[i] == 1) {
                            el.style.color = "blue";
                            el.innerHTML += "<input gameval='" + i + "'type='button' class='btn btn-success pull-right' value='Join Game'></input>";
                        } else {
                            el.style.color = "red";
                            el.innerHTML += "<input gameval='" + i + "'type='button' class='btn btn-default pull-right' value='Spectate'></input>";
                        }
                    } catch(e) {
                        console.error("Game data not available");
                    }
                }
            }
        });
    }, 5000);

    /**
     *
     */
    document.addEventListener("click", function(event){
        if (event.target.type == "button"){
            if (event.target.value == "Join Game"){
                var game_num = event.target.getAttribute('gameval');
            } else if (event.target.value == "Spectate"){
                var game_num = event.target.getAttribute('gameval');
            } else if (event.target.value == "Join New Game") {
                $.ajax({
                    type: "POST",
                    url: "/",
                    success: function(data) {
                        data = JSON.parse(data);
                        if (data == "error") {
                            /* here, we want to trigger some box saying no game is available */
                            createNoGamesAlert();

                        } else {
                            window.location.href = data;
                        }
                    }
                });
            } else if (event.target.value == "Create New Game") {
                $.ajax({
                    type: "POST",
                    url: "/create_game",
                    success: function(data) {
                        if (data == "success") {
                            createNewGameAlert();
                        } else if (data == "error") {
                            createErrorAlert("An Error has Occured");
                        }
                    }
                });
            }
        }
    });
