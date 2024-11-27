$(document).ready(function() {
    var predictedMoviesData = []; // Variable to store predicted movies data
  
    // Autocomplete functionality for the search box
    $(function() {
      $("#searchBox").autocomplete({
        source: function(request, response) {
          $.ajax({
            type: "POST",
            url: "/search",
            dataType: "json",
            cache: false,
            data: {
              q: request.term,
            },
            success: function(data) {
              response(data);
            },
            error: function(jqXHR, textStatus, errorThrown) {
              console.log(textStatus + " " + errorThrown);
            },
          });
        },
        select: function(event, ui) {
          var ulList = $("#selectedMovies");
          // Check if the value already exists in the list
          if (ulList.find('li:contains("' + ui.item.value + '")').length > 0) {
            $("#searchBox").val("");
            return false;
          }
          var deleteButton = $("<button type='button' class='btn btn-danger btn-sm'>Delete</button>");
          // Attach click event to the delete button
          deleteButton.click(function() {
            $(this).closest('li').remove(); // Removes the parent <li> of the button
          });
  
          var li = $("<li class='list-group-item d-flex justify-content-between align-items-center'/>")
            .text(ui.item.value)
            .append(deleteButton)
            .appendTo(ulList);
          $("#searchBox").val("");
          return false;
        },
        minLength: 1,
      });
    });
  
    // Function to fetch poster URL
    function fetchPosterURL(imdbID) {
      var posterURL = null;
      $.ajax({
        type: "GET",
        url: "/getPosterURL",
        dataType: "json",
        data: { imdbID: imdbID },
        async: false,
        success: function(response) {
          posterURL = response.posterURL;
        },
        error: function(error) {
          console.log("Error fetching poster URL: " + error);
        },
      });
      return posterURL;
    }
  
    // Click event handler for the Predict button
    $("#predict").click(function() {
      $("#loader").attr("class", "d-flex justify-content-center");
  
      var movie_list = [];
      $("#selectedMovies li").each(function() {
        movie_list.push($(this).text());
      });
  
      var selected_genre = $("#genreSelect").val(); // Get the selected genre
      var release_year = $("#releaseYear").val();
      if (release_year) {
        release_year = parseInt(release_year);
      }
      var movies = { movie_list: movie_list, genre: selected_genre, year: release_year };
  
      // Clear the existing recommendations
      $("#predictedMovies").empty();
  
      // Check if at least one movie is selected
      if (movie_list.length == 0) {
        alert("Select at least 1 movie!!");
        $("#loader").attr("class", "d-none");
        return;
      }
  
      // AJAX request to get predicted movies
      $.ajax({
        type: "POST",
        url: "/predict",
        dataType: "json",
        contentType: "application/json;charset=UTF-8",
        traditional: "true",
        cache: false,
        data: JSON.stringify(movies),
        success: function(response) {
          var data = JSON.parse(response);
          predictedMoviesData = data; // Store data for sorting later
  
          // Show the sort filter since we now have predicted movies
          $("#sortFilter").show();
  
          // Render the predicted movies
          renderPredictedMovies(predictedMoviesData);
  
          $("#loader").attr("class", "d-none");
        },
        error: function(error) {
          console.log("ERROR ->" + error);
          $("#loader").attr("class", "d-none");
        },
      });
    });
  
    // Function to render predicted movies
    function renderPredictedMovies(data) {
      var list = $("#predictedMovies");
      list.empty(); // Clear existing movies
      var modalParent = document.getElementById("modalParent");
      modalParent.innerHTML = ""; // Clear existing modals
      var row = $('<div class="row"></div>');
  
      for (var i = 0; i < data.length; i++) {
        if (i > 0 && i % 3 === 0) {
          // After every 3 movies, append the row to the list and create a new row
          list.append(row);
          row = $('<div class="row"></div>'); // Create a new row for the next set of 3 movies
        }
        var column = $('<div class="col-md-4"></div>');
        var card = `<div class="card movie-card">
          <div class="row no-gutters">
            <div class="col-md-6">
              <div class="card-body">
                <a type="button" class="btn btn-warning ms-2" href="/movies?movie_id=${data[i].movieId}">${data[i].title}</a>
                <h6 class="card-subtitle mb-2 text-muted">${data[i].runtime} minutes</h6>
                <p class="card-text" hidden>${data[i].overview}</p>
                <a target="_blank" href="/movies?movie_id=${data[i].movieId}" class="btn btn-primary" hidden>Check out the movie!</a>
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" id="modalButton-${i}" data-bs-target="#reviewModal-${i}">Write a review</button>
                <div class="movieId" hidden>${data[i].movieId}</div>
                <div class="genres" hidden>${data[i].genres}</div>
                <div class="imdb_id" hidden>${data[i].imdb_id}</div>
                <div class="poster_path" hidden>${data[i].poster_path}</div>
                <div class="index" hidden>${i}</div>
              </div>
            </div>
            <div class="col-md-6">
                <img src="${fetchPosterURL(data[i].imdb_id)}" alt="Movie Poster" class="poster-image" style="width: 75%; height: auto; margin: 0;">
            </div>
          </div>
        </div>`;
        var modal = `
        <div class="modal fade" id="reviewModal-${i}" tabindex="-1" aria-labelledby="reviewModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="reviewModaLabel">Write your review</h5>
                <button type="button" onclick="modalOnClose(${i})" id="closeModal-${i}" class="btn-close" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <div class="mb-3">
                  <textarea class="form-control" rows=10 id="review-${i}"></textarea>
                </div>
                <div class="mb-3">
                  <label for="score-${i}" class="form-label">Select Score:</label>
                  <select class="form-select" id="score-${i}">
                      <option value="1.0">1.0</option>
                      <option value="2.0">2.0</option>
                      <option value="3.0">3.0</option>
                      <option value="4.0">4.0</option>
                      <option value="5.0">5.0</option>
                  </select>
                </div>
              </div>
              <div class="modal-footer">
                <button type="button" onclick="modalOnClick(${i})" id="saveChanges-${i}" class="btn btn-primary modal-save">Save changes</button>
              </div>
            </div>
          </div>
        </div>`;
        modalParent.innerHTML += modal;
        column.append(card);
        row.append(column);
      }
      list.append(row);
    }
  
    // Event listener for sorting by runtime
    $("#runtimeSort").on('change', function() {
      var sortOrder = $(this).val();
      var sortedData = predictedMoviesData.slice(); // Copy the array to avoid mutating original data
      if (sortOrder === 'asc') {
        sortedData.sort(function(a, b) {
          return a.runtime - b.runtime;
        });
      } else if (sortOrder === 'desc') {
        sortedData.sort(function(a, b) {
          return b.runtime - a.runtime;
        });
      }
      renderPredictedMovies(sortedData);
    });
  
    // Modal event handler for saving reviews
    modalOnClick = (i) => {
      var main_element = $(`#modalButton-${i}`).siblings();
      var data = {
        title: main_element[0].textContent,
        runtime: parseInt(main_element[1].textContent),
        overview: main_element[2].textContent,
        movieId: main_element[4].textContent,
        genres: main_element[5].textContent,
        imdb_id: main_element[6].textContent,
        poster_path: main_element[7].textContent,
        review_text: $(`#review-${i}`)[0].value,
        score: $(`#score-${i}`).val(),
      };
      $.ajax({
        type: "POST",
        url: "/postReview",
        dataType: "json",
        contentType: "application/json;charset=UTF-8",
        traditional: "true",
        cache: false,
        data: JSON.stringify(data),
        success: (response) => {
          $(`#reviewModal-${i}`).modal('toggle');
          $(`#review-${i}`).val("");
          $(`#score-${i}`).val("1.0");
          $("#saved-flash").attr("hidden", false);
        },
        error: function(jqXHR, textStatus, errorThrown) {
          // Parse error response
          const errorData = JSON.parse(jqXHR.responseText);
          const errorMessage = errorData.message;
  
          // Display error message
          alert(`Error: ${errorMessage}`);
        },
      });
    };
  
    // Modal event handler for closing the review modal
    modalOnClose = (i) => {
      $(`#reviewModal-${i}`).modal('toggle');
    };
  
    // Event listener for the back button
    window.addEventListener("popstate", function(event) {
      // Check if the user is navigating back
      if (event.state && event.state.page === "redirect") {
        // Redirect the user to a specific URL
        window.location.href = "/";
        location.reload();
      }
    });
  });
  