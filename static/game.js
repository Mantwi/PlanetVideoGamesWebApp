$(function() {
    $.ajax({
        url: '/get_popular_games',
        type: 'GET',
        success: function(response) {
            let gamesListHtml = '<ul>';
            response.forEach(function(game) {
                gamesListHtml += `<li><a href="/view/${game.id}">${game.title}</a></li>`;
            });
            gamesListHtml += '</ul>';
            $('#popular-games').html(gamesListHtml);
        },
        error: function(error) {
            console.log(error);
        }
    });

    $('#searchForm').on('submit', function(e) {
        var searchQuery = $('#searchInput').val().trim();
        if (!searchQuery) {
            e.preventDefault(); 
            $('#searchInput').val('').focus();
        }
    });
});
