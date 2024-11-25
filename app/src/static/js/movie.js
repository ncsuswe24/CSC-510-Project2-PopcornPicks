
$(document).ready(function () {
    function fetchPosterURL(obj) {
        $.ajax({
            type: "GET",
            url: "/getPosterURL", 
            dataType: "json",
            data: { imdbID: obj.innerHTML },
            async: false, 
            success: function (response) {
                var posterHTML = `<img src="${response.posterURL}" alt="Movie Poster" class="poster-image" style="width: 75%; height: auto; margin: 0;">`;
                obj.innerHTML += posterHTML;        
            },
            error: function (error) {
                console.log("Error fetching poster URL: " + error);
            },
        });
    }

    $('.imdbId').each((index, obj) => {
        fetchPosterURL(obj);
    });

    $('.like-dislike-buttons').each(function() {
        var container = $(this);
        var movieId = container.data('movie-id');
        var likeButton = container.find('#like-button');
        var dislikeButton = container.find('#dislike-button');

        likeButton.click(function() {
            sendLikeDislike(movieId, 1, likeButton, dislikeButton);
        });

        dislikeButton.click(function() {
            sendLikeDislike(movieId, -1, likeButton, dislikeButton);
        });
    });

    function sendLikeDislike(movieId, likeValue, likeButton, dislikeButton) {
        $.ajax({
            type: "POST",
            url: "/like",
            contentType: "application/json",
            data: JSON.stringify({
                'movieId': movieId,
                'like_value': likeValue
            }),
            success: function(response) {
                likeButton.text('Like (' + response.likes_count + ')');
                dislikeButton.text('Dislike (' + response.dislikes_count + ')');
                likeButton.prop('disabled', true);
                dislikeButton.prop('disabled', true);
            },
            error: function(error) {
                console.log('Error:', error);
            }
        });
    }
});
