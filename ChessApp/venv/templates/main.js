function submitMove(curr_game) {
    var httpRequest = XMLHttpRequest();
    httpRequest.onreadystatechange = function() {
        // This will run once we get a response from the server
        alert('hello');
    }
    // If asynchronous call is required, set third parameter to true
    httpRequest.open('POST', '/game/' + curr_game);
    httpRequest.send('hello');

    return "hello";
}