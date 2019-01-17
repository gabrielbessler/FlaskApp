function submitMove(curr_game) {
    $.ajax({
        type:"POST",
        url:'/ajax',
        success: function(data) {
            data = JSON.parse(data);
            document.body.innerHTML = data;
        }
    })
}