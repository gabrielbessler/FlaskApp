function submitMove(curr_game) {
    var httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = function(data) {
        // This will run once we get a response from the server
        //document.getElementById("display_board").style.backgroundColor = "blue";
        alert(data);
    }
    // If asynchronous call is required, set third parameter to true
    httpRequest.open('POST', '/ajax');
    httpRequest.send();

    return '0';
}