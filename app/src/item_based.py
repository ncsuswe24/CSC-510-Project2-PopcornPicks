"""
Copyright (c) 2023 Abhinav Sinha, Chandana Ray, Sam Kwiatkowski-Martin, Tanmay Pardeshi
This code is licensed under MIT license (see LICENSE for details)

@author: PopcornPicks
"""

import os
import re
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app_dir = os.path.dirname(os.path.abspath(__file__))
code_dir = os.path.dirname(app_dir)
project_dir = os.path.dirname(code_dir)


def extract_year_from_title(title):
    """
    Extracts the year from a movie title string.
    """
    match = re.search(r'\((\d{4})\)', title)
    if match:
        return int(match.group(1))  # Extract the year as an integer
    return None


def recommend_for_new_user(user_rating, selected_genre=None, selected_year=None):
    """
    Generates a list of recommended movie titles for a new user based on their ratings.
    """
    # Return empty DataFrame if no user ratings are provided
    default = pd.DataFrame(
            columns=[
                "movieId", "title", "genres", "imdb_id", "overview",
                "poster_path", "runtime", "recommended"
            ]
        )

    if not user_rating:
        return default

    # Load movies dataset and embeddings
    movies = pd.read_csv(os.path.join(project_dir, "data", "movies.csv"))
    embeddings = np.load(
        os.path.join(project_dir, "data", "movie_embeddings.npz"))['embeddings']
    # np.savez_compressed("embeddings.npz", embeddings=embeddings)
    user_ratings_df = pd.DataFrame(user_rating)  # Expects keys: 'movieId', 'rating'

    # Find the row indices for the user-rated movies in the movies dataset
    user_indices = movies[movies['title'].isin(user_ratings_df['title'])].index.to_numpy()

    # Extract the corresponding embeddings and ratings
    user_embeddings = embeddings[user_indices]
    user_ratings = user_ratings_df['rating'].to_numpy().reshape(-1, 1)  # Column vector of ratings

    # Compute the weighted sum of embeddings
    user_profile = np.sum(user_embeddings * user_ratings, axis=0) / user_ratings.sum()

    # Filter by genre if specified
    if selected_genre:
        movies = movies[
            movies["genres"].str.contains(selected_genre, case=False, na=False)
        ]
    # Filter by year if specified
    if selected_year:
        movies = movies[
            movies["title"].apply(lambda x: extract_year_from_title(x) == selected_year)
        ]

    if movies.empty:
        return default

    # Compute similarity between user profile and all movie embeddings
    embeddings = embeddings[movies.index.to_numpy()]
    similarities = cosine_similarity([user_profile], embeddings).flatten()

    # Get top recommendations, exclude movies the user has already rated, sort by similarity score.
    movies['similarity'] = similarities
    recommendations = movies[~movies.index.isin(user_indices)]
    recommendations = recommendations.sort_values(by='similarity', ascending=False)

    # Return top 10 recommendations
    return recommendations.head(9)
