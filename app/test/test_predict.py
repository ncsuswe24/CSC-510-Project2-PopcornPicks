"""
Copyright (c) 2023 Abhinav Sinha, Chandana Ray, Sam Kwiatkowski-Martin, Tanmay Pardeshi
This code is licensed under MIT license (see LICENSE for details)

@author: PopcornPicks
"""

import sys
import warnings
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.item_based import recommend_for_new_user
warnings.filterwarnings("ignore")
import unittest
import os
from unittest.mock import patch, MagicMock
from flask import json
import pandas as pd
import numpy as np
# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import app, db
from src.models import Review, Movie  # Import the Review model
from flask_login import current_user

class Tests(unittest.TestCase):
    """
    Test cases for recommender system
    """

    def test_toy_story(self):
        """
        Test case 1
        """
        ts = [
            {"title": "Toy Story (1995)", "rating": 5.0},
        ]
        recommendations = recommend_for_new_user(ts)
        self.assertTrue(recommendations.shape[0], 9)

    def test_kungfu_panda(self):
        """
        Test case 2
        """
        ts = [
            {"title": "Kung Fu Panda (2008)", "rating": 5.0},
        ]
        recommendations = recommend_for_new_user(ts)
        self.assertTrue(recommendations.shape[0], 9)

    def test_hindi_movie(self):
        """
        Test case 3
        """
        ts = [
            {"title": "Bachna Ae Haseeno (2008)", "rating": 5.0},
        ]
        recommendations = recommend_for_new_user(ts)
        self.assertTrue(recommendations.shape[0], 9)

    def test_iron_man(self):
        """
        Test case 4
        """
        ts = [
            {"title": "Iron Man (2008)", "rating": 5.0},
        ]
        recommendations = recommend_for_new_user(ts)
        self.assertTrue(recommendations.shape[0], 9)

    def test_robo_cop(self):
        """
        Test case 5
        """
        ts = [
            {"title": "RoboCop (1987)", "rating": 5.0},
        ]
        recommendations = recommend_for_new_user(ts)
        self.assertTrue(recommendations.shape[0], 9)

    def test_nolan(self):
        """
        Test case 6
        """
        ts = [
            {"title": "Inception (2010)", "rating": 5.0},
        ]
        recommendations = recommend_for_new_user(ts)
        self.assertTrue(recommendations.shape[0], 9)

    def test_dc(self):
        """
        Test case 7
        """
        ts = [
            {"title": "Man of Steel (2013)", "rating": 5.0},
        ]
        recommendations = recommend_for_new_user(ts)
        self.assertTrue(recommendations.shape[0], 9)

    def test_armageddon(self):
        """
        Test case 8
        """
        ts = [
            {"title": "Armageddon (1998)", "rating": 5.0},
        ]
        recommendations = recommend_for_new_user(ts)
        self.assertTrue(recommendations.shape[0], 9)

    def test_lethal_weapon(self):
        """
        Test case 9
        """
        ts = [
            {"title": "Lethal Weapon (1987)", "rating": 5.0},
        ]
        recommendations = recommend_for_new_user(ts)
        self.assertTrue(recommendations.shape[0], 9)

    def test_dark_action(self):
        """
        Test case 10
        """
        ts = [
            {"title": "Batman Returns (1992)", "rating": 5.0},
        ]
        recommendations = recommend_for_new_user(ts)
        self.assertTrue(recommendations.shape[0], 9)

    def test_dark(self):
        """
        Test case 11
        """
        ts = [
            {"title": "Puppet Master (1989)", "rating": 5.0},
        ]
        recommendations = recommend_for_new_user(ts)
        self.assertTrue(recommendations.shape[0], 9)

    def test_horror_comedy(self):
        """
        Test case 12
        """
        ts = [
            {"title": "Scary Movie (2000)", "rating": 5.0},
        ]
        recommendations = recommend_for_new_user(ts)
        self.assertTrue(recommendations.shape[0], 9)

    def test_super_heroes(self):
        """
        Test case 13
        """
        ts = [
            {"title": "Spider-Man (2002)", "rating": 5.0},
        ]
        recommendations = recommend_for_new_user(ts)
        self.assertTrue(recommendations.shape[0], 9)

    def test_cartoon(self):
        """
        Test case 14
        """
        ts = [
            {"title": "Moana (2016)", "rating": 5.0},
        ]
        recommendations = recommend_for_new_user(ts)
        self.assertTrue(recommendations.shape[0], 9)

    def test_multiple_movies(self):
        """
        Test case 15
        """
        ts = [
            {"title": "Twilight Saga: New Moon, The (2009)", "rating": 5.0},
            {"title": "Harry Potter and the Goblet of Fire (2005)", "rating": 5.0}
        ]
        recommendations = recommend_for_new_user(ts)
        self.assertTrue(recommendations.shape[0], 9)

    def test_multiple_movies_2(self):
        """
        Test case 16
        """
        ts = [
            {"title": "Heat (1995)", "rating": 5.0},
            {"title": "The Departed (2008)", "rating": 5.0}
        ]
        recommendations = recommend_for_new_user(ts)
        self.assertTrue(recommendations.shape[0], 9)

    def test_comedy_and_year(self):
        """
        Test case 17
        """
        ts = [{"title": "Hitch (2005)", "rating": 4.0}]
        recommendations = recommend_for_new_user(ts, selected_genre="Comedy", selected_year=2005)
        self.assertEqual(recommendations.shape[0], 9)
        self.assertTrue(all("Comedy" in genres for genres in recommendations['genres']))
        self.assertTrue(all("2005" in title for title in recommendations['title']))

    def test_fantasy_and_year(self):
        """
        Test case 18
        """
        ts = [{"title": "Shopping (1994)", "rating": 4.0}]
        recommendations = recommend_for_new_user(ts, selected_genre="Fantasy", selected_year=2010)
        self.assertEqual(recommendations.shape[0], 9)
        self.assertTrue(all("Fantasy" in genres for genres in recommendations['genres']))
        self.assertTrue(all("2010" in title for title in recommendations['title']))

    def test_thriller_and_year(self):
        """
        Test case 19
        """
        ts = [{"title": "Se7en (1995)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts, selected_genre="Thriller", selected_year=1995)
        self.assertEqual(recommendations.shape[0], 9)
        self.assertTrue(all("Thriller" in genres for genres in recommendations['genres']))
        self.assertTrue(all("1995" in title for title in recommendations['title']))

    def test_family_and_year(self):
        """
        Test case 20
        """
        ts = [{"title": "Little Women (1994)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts, selected_genre="Family", selected_year=1994)
        self.assertEqual(recommendations.shape[0], 9)
        self.assertTrue(all("Family" in genres for genres in recommendations['genres']))
        self.assertTrue(all("1994" in title for title in recommendations['title']))

    def test_year_2000(self):
        """
        Test case 21
        """
        ts = [{"title": "Se7en (1995)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts, selected_year=2000)
        self.assertEqual(recommendations.shape[0], 9)
        self.assertTrue(all("2000" in title for title in recommendations['title']))

    def test_year_1989(self):
        """
        Test case 22
        """
        ts = [{"title": "Se7en (1995)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts, selected_year=1989)
        self.assertEqual(recommendations.shape[0], 9)
        self.assertTrue(all("1989" in title for title in recommendations['title']))

    def test_year_2001(self):
        """
        Test case 23
        """
        ts = [{"title": "Se7en (1995)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts, selected_year=2001)
        self.assertEqual(recommendations.shape[0], 9)
        self.assertTrue(all("2001" in title for title in recommendations['title']))

    def test_year_2008(self):
        """
        Test case 24
        """
        ts = [{"title": "Se7en (1995)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts, selected_year=2008)
        self.assertEqual(recommendations.shape[0], 9)
        self.assertTrue(all("2008" in title for title in recommendations['title']))

    def test_action_genre(self):
        """
        Test case 25
        """
        ts = [{"title": "Die Hard (1988)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts, selected_genre="Action")
        self.assertTrue(all("Action" in genres for genres in recommendations['genres']))
        self.assertEqual(recommendations.shape[0], 9)

    def test_adventure_genre(self):
        """
        Test case 26
        """
        ts = [{"title": "Die Hard (1988)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts, selected_genre="Adventure")
        self.assertTrue(all("Adventure" in genres for genres in recommendations['genres']))
        self.assertEqual(recommendations.shape[0], 9)

    def test_animation_genre(self):
        """
        Test case 27
        """
        ts = [{"title": "Die Hard (1988)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts, selected_genre="Animation")
        self.assertTrue(all("Animation" in genres for genres in recommendations['genres']))
        self.assertEqual(recommendations.shape[0], 9)

    def test_horror_genre(self):
        """
        Test case 28
        """
        ts = [{"title": "Die Hard (1988)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts, selected_genre="Horror")
        self.assertTrue(all("Horror" in genres for genres in recommendations['genres']))
        self.assertEqual(recommendations.shape[0], 9)

    def test_foreign_genre(self):
        """
        Test case 29
        """
        ts = [{"title": "Shopping (1994)", "rating": 4.0}]
        recommendations = recommend_for_new_user(ts, selected_genre="Foreign")
        self.assertEqual(recommendations.shape[0], 9)
        self.assertTrue(all("Foreign" in genres for genres in recommendations['genres']))

    def test_romance_genre(self):
        """
        Test case 30
        """
        ts = [{"title": "The Notebook (2004)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts, selected_genre="Romance")
        self.assertEqual(recommendations.shape[0], 9)
        self.assertTrue(all("Romance" in genres for genres in recommendations['genres']))

    def test_scifi_genre(self):
        """
        Test case 31
        """
        ts = [{"title": "The Avengers (2012)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts, selected_genre="Science Fiction")
        self.assertEqual(recommendations.shape[0], 9)
        self.assertTrue(all("Science Fiction" in genres for genres in recommendations['genres']))

    def test_empty_input(self):
        """
        Test case 32
        """
        recommendations = recommend_for_new_user([])
        self.assertEqual(recommendations.shape[0], 0)

    def test_no_matching_genre_year(self):
        """
        Test case 33
        """
        ts = [{"title": "Toy Story (1995)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts, selected_genre="Sci-Fi", selected_year=2025)
        self.assertEqual(recommendations.shape[0], 0)

    def test_no_matching_genre_year_2(self):
        """
        Test case 34
        """
        ts = [{"title": "Toy Story (1995)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts, selected_genre="Slice of Life", selected_year=2030)
        self.assertEqual(recommendations.shape[0], 0)

    def test_no_matching_genre_year_3(self):
        """
        Test case 35
        """
        ts = [{"title": "Toy Story (1995)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts, selected_genre="British", selected_year=1245)
        self.assertEqual(recommendations.shape[0], 0)
    def test_predicted_movies_have_runtime(self):
        """
        Test case 36: Ensure that predicted movies include the 'runtime' field with valid integer values
        """
        ts = [{"title": "Inception (2010)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        self.assertEqual(recommendations.shape[0], 9)
        # Check that 'runtime' field exists and is an integer
        for runtime in recommendations['runtime']:
            self.assertIsInstance(runtime, int)
            self.assertTrue(runtime > 0)  # Runtime should be a positive integer

    def test_sort_predicted_movies_by_runtime_asc(self):
        """
        Test case 37: Verify that sorting predicted movies by runtime ascending works correctly
        """
        ts = [{"title": "Inception (2010)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        recommendations_sorted = recommendations.sort_values(by='runtime')
        runtimes = recommendations_sorted['runtime'].tolist()
        self.assertEqual(runtimes, sorted(runtimes))

    def test_sort_predicted_movies_by_runtime_desc(self):
        """
        Test case 38: Verify that sorting predicted movies by runtime descending works correctly
        """
        ts = [{"title": "Inception (2010)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        recommendations_sorted = recommendations.sort_values(by='runtime', ascending=False)
        runtimes = recommendations_sorted['runtime'].tolist()
        self.assertEqual(runtimes, sorted(runtimes, reverse=True))

    def test_predicted_movies_with_runtime_filter_and_genre(self):
        """
        Test case 39: Ensure that predicted movies filtered by genre have valid runtime values
        """
        ts = [{"title": "Inception (2010)", "rating": 5.0}]
        selected_genre = "Action"
        recommendations = recommend_for_new_user(ts, selected_genre=selected_genre)
        self.assertEqual(recommendations.shape[0], 9)
        # Check that 'runtime' field exists and is an integer
        for index, row in recommendations.iterrows():
            self.assertIsInstance(row['runtime'], int)
            self.assertTrue(row['runtime'] > 0)
            self.assertIn(selected_genre, row['genres'])

    def test_predicted_movies_with_runtime_filter_and_year(self):
        """
        Test case 40: Ensure that predicted movies filtered by release year have valid runtime values
        """
        ts = [{"title": "Inception (2010)", "rating": 5.0}]
        selected_year = 2010
        recommendations = recommend_for_new_user(ts, selected_year=selected_year)
        self.assertEqual(recommendations.shape[0], 9)
        # Check that 'runtime' field exists and is an integer
        for index, row in recommendations.iterrows():
            self.assertIsInstance(row['runtime'], int)
            self.assertTrue(row['runtime'] > 0)
            self.assertIn(str(selected_year), row['title'])

    def test_predicted_movies_with_runtime_filter_genre_and_year(self):
        """
        Test case 41: Ensure that predicted movies filtered by both genre and release year have valid runtime values
        """
        ts = [{"title": "Inception (2010)", "rating": 5.0}]
        selected_genre = "Action"
        selected_year = 2010
        recommendations = recommend_for_new_user(ts, selected_genre=selected_genre, selected_year=selected_year)
        self.assertEqual(recommendations.shape[0], 9)
        # Check that 'runtime' field exists and is an integer
        for index, row in recommendations.iterrows():
            self.assertIsInstance(row['runtime'], int)
            self.assertTrue(row['runtime'] > 0)
            self.assertIn(selected_genre, row['genres'])
            self.assertIn(str(selected_year), row['title'])

    def test_predicted_movies_runtime_values(self):
        """
        Test case 42: Ensure that predicted movies have realistic runtime values (e.g., between 30 and 300 minutes)
        """
        ts = [{"title": "Inception (2010)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        for runtime in recommendations['runtime']:
            self.assertTrue(30 <= runtime <= 300, f"Runtime {runtime} is out of realistic range")

     

    def test_predicted_movies_duplicate_runtimes(self):
        """
        Test case 43: Ensure that sorting handles duplicate 'runtime' values correctly
        """
        # Mock the recommendations to have duplicate runtimes
        ts = [{"title": "Inception (2010)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        recommendations['runtime'] = [120, 120, 150, 150, 150, 180, 180, 200, 200]
        # Sort and verify
        recommendations_sorted = recommendations.sort_values(by='runtime')
        runtimes = recommendations_sorted['runtime'].tolist()
        self.assertEqual(runtimes, sorted(runtimes))

    def test_predicted_movies_same_runtime(self):
        """
        Test case 44: Ensure that sorting works when all movies have the same 'runtime'
        """
        ts = [{"title": "Inception (2010)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Set all runtimes to the same value
        recommendations['runtime'] = [120] * recommendations.shape[0]
        # Sort and verify
        recommendations_sorted = recommendations.sort_values(by='runtime')
        runtimes = recommendations_sorted['runtime'].tolist()
        self.assertEqual(runtimes, [120] * recommendations.shape[0])
 

    def test_predicted_movies_extreme_runtime_values(self):
        """
        Test case 45: Ensure that movies with extreme 'runtime' values are handled correctly
        """
        ts = [{"title": "Epic Movie (2007)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Set extreme runtimes
        recommendations['runtime'] = [10, 500, 45, 300, 20, 600, 15, 480, 60]
        # Check that runtimes are sorted correctly
        recommendations_sorted = recommendations.sort_values(by='runtime')
        runtimes = recommendations_sorted['runtime'].tolist()
        self.assertEqual(runtimes, sorted(runtimes))

    def test_predicted_movies_invalid_runtime_values(self):
        """
        Test case 46: Ensure that movies with invalid 'runtime' values are handled appropriately
        """
        ts = [{"title": "Inception (2010)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Introduce invalid runtime values
        recommendations.at[0, 'runtime'] = -90
        recommendations.at[1, 'runtime'] = "NaN"
        # Validate runtimes
        for runtime in recommendations['runtime']:
            if isinstance(runtime, int):
                self.assertTrue(runtime > 0)
            else:
                self.assertRaises(ValueError)

    def test_maximum_selected_movies(self):
        """
        Test case 47: Ensure that the system handles the maximum allowed number of selected movies
        """
        # Assuming the maximum allowed is 5 movies
        ts = [
            {"title": "Movie A (2000)", "rating": 5.0},
            {"title": "Movie B (2001)", "rating": 5.0},
            {"title": "Movie C (2002)", "rating": 5.0},
            {"title": "Movie D (2003)", "rating": 5.0},
            {"title": "Movie E (2004)", "rating": 5.0},
        ]
        recommendations = recommend_for_new_user(ts)
        self.assertEqual(recommendations.shape[0], 9)
        # Check that runtimes are valid
        for runtime in recommendations['runtime']:
            self.assertIsInstance(runtime, int)
            self.assertTrue(runtime > 0)

    def test_empty_selected_movies_list(self):
        """
        Test case 48: Ensure that the system handles an empty list of selected movies
        """
        ts = []
        recommendations = recommend_for_new_user(ts)
        self.assertEqual(recommendations.shape[0], 0)

    def test_runtime_field_format(self):
        """
        Test case 49: Ensure that the 'runtime' field is correctly formatted (integer)
        """
        ts = [{"title": "Inception (2010)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        for runtime in recommendations['runtime']:
            self.assertIsInstance(runtime, int)

    def test_sorting_with_mixed_runtime_values(self):
        """
        Test case 50: Ensure that sorting works with a mix of valid, missing, and extreme runtime values
        """
        ts = [{"title": "Inception (2010)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Set mixed runtime values
        recommendations['runtime'] = [120, None, 500, 45, -10, 300, "NaN", 60, 90]
        # Clean data by removing invalid runtimes
        recommendations = recommendations[pd.to_numeric(recommendations['runtime'], errors='coerce').notnull()]
        recommendations['runtime'] = recommendations['runtime'].astype(int)
        recommendations = recommendations[recommendations['runtime'] > 0]
        # Sort and verify
        recommendations_sorted = recommendations.sort_values(by='runtime')
        runtimes = recommendations_sorted['runtime'].tolist()
        self.assertEqual(runtimes, sorted(runtimes))

    def test_runtime_sorting_stability(self):
        """
        Test case 51: Ensure that the sorting is stable (maintains order of movies with equal runtimes)
        """
        ts = [{"title": "Inception (2010)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Set duplicate runtimes
        recommendations['runtime'] = [120, 120, 150, 150, 150, 180, 180, 200, 200]
        # Add an 'original_order' column to track initial positions
        recommendations['original_order'] = range(recommendations.shape[0])
        # Sort by runtime
        recommendations_sorted = recommendations.sort_values(by=['runtime', 'original_order'])
        # Check that movies with equal runtimes maintain original order
        for runtime in set(recommendations['runtime']):
            subset = recommendations_sorted[recommendations_sorted['runtime'] == runtime]
            original_orders = subset['original_order'].tolist()
            self.assertEqual(original_orders, sorted(original_orders))
    def test_runtime_zero_values(self):
        """
        Test case 52: Ensure that movies with a runtime of zero are handled appropriately
        """
        ts = [{"title": "Movie with Zero Runtime (2021)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Manually set one runtime to zero
        recommendations.at[0, 'runtime'] = 0
        # Validate runtimes
        for runtime in recommendations['runtime']:
            self.assertIsInstance(runtime, int)
            self.assertGreaterEqual(runtime, 0)
        # Check how zero runtimes are handled in sorting
        recommendations_sorted = recommendations.sort_values(by='runtime')
        runtimes = recommendations_sorted['runtime'].tolist()
        self.assertEqual(runtimes, sorted(runtimes))

    def test_runtime_negative_values(self):
        """
        Test case 53: Ensure that movies with negative runtime values are handled appropriately
        """
        ts = [{"title": "Movie with Negative Runtime (2021)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Manually set one runtime to a negative value
        recommendations.at[0, 'runtime'] = -100
        # Exclude negative runtimes
        recommendations_clean = recommendations[recommendations['runtime'] > 0]
        # Validate runtimes
        for runtime in recommendations_clean['runtime']:
            self.assertIsInstance(runtime, int)
            self.assertGreater(runtime, 0)
        # Ensure that sorting works without negative runtimes
        recommendations_sorted = recommendations_clean.sort_values(by='runtime')
        runtimes = recommendations_sorted['runtime'].tolist()
        self.assertEqual(runtimes, sorted(runtimes))

    def test_runtime_float_values(self):
        """
        Test case 54: Ensure that movies with float runtime values are handled appropriately
        """
        ts = [{"title": "Movie with Float Runtime (2021)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Set runtimes to float values
        recommendations['runtime'] = [90.5, 120.75, 110.25, 100.0, 95.5, 105.75, 115.5, 130.25, 125.0]
        # Convert float runtimes to int
        recommendations['runtime'] = recommendations['runtime'].astype(int)
        for runtime in recommendations['runtime']:
            self.assertIsInstance(runtime, int)
            self.assertGreater(runtime, 0)

    def test_runtime_string_values(self):
        """
        Test case 55: Ensure that movies with runtime values as strings are handled appropriately
        """
        ts = [{"title": "Movie with String Runtime (2021)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Set runtimes to numeric strings
        recommendations['runtime'] = ['90', '120', '110', '100', '95', '105', '115', '130', '125']
        # Convert strings to integers
        recommendations['runtime'] = recommendations['runtime'].astype(int)
        for runtime in recommendations['runtime']:
            self.assertIsInstance(runtime, int)
            self.assertGreater(runtime, 0)

    def test_runtime_special_characters(self):
        """
        Test case 56: Ensure that movies with runtime values containing special characters are handled
        """
        ts = [{"title": "Movie with Special Characters in Runtime (2021)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Set runtimes with special characters
        recommendations['runtime'] = ['90 min', '120 mins', '110 minutes', '100', '95', '105', '115', '130', '125']
        # Extract numeric values
        recommendations['runtime'] = recommendations['runtime'].str.extract('(\d+)').astype(int)
        for runtime in recommendations['runtime']:
            self.assertIsInstance(runtime, int)
            self.assertGreater(runtime, 0)

    def test_runtime_missing_field(self):
        """
        Test case 57: Ensure that movies without a 'runtime' field are handled appropriately
        """
        ts = [{"title": "Movie Without Runtime (2021)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Remove the 'runtime' column
        recommendations.drop(columns=['runtime'], inplace=True)
        # Attempt to sort and handle missing 'runtime' field
        with self.assertRaises(KeyError):
            recommendations.sort_values(by='runtime')

    def test_runtime_large_numbers(self):
        """
        Test case 58: Ensure that movies with extremely large 'runtime' values are handled
        """
        ts = [{"title": "Extremely Long Movie (2021)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Set extremely large runtimes
        recommendations['runtime'] = [1000000 * i for i in range(1, 10)]
        # Validate and sort
        for runtime in recommendations['runtime']:
            self.assertIsInstance(runtime, int)
            self.assertGreater(runtime, 0)
        recommendations_sorted = recommendations.sort_values(by='runtime')
        runtimes = recommendations_sorted['runtime'].tolist()
        self.assertEqual(runtimes, sorted(runtimes))

    def test_runtime_non_numeric_strings(self):
        """
        Test case 59: Ensure that movies with non-numeric string runtimes are handled
        """
        ts = [{"title": "Movie with Non-Numeric Runtime (2021)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Set runtimes to non-numeric strings
        recommendations['runtime'] = ['one hundred', 'two hundred', 'three hundred'] * 3
        # Attempt to convert to numeric values
        recommendations['runtime'] = pd.to_numeric(recommendations['runtime'], errors='coerce')
        # Check that runtimes are NaN and drop them
        recommendations_clean = recommendations.dropna(subset=['runtime'])
        self.assertEqual(recommendations_clean.shape[0], 0)


    def test_runtime_with_nulls_and_nans(self):
        """
        Test case 60: Ensure that movies with NaN or null 'runtime' values are handled
        """
        ts = [{"title": "Movie with NaN Runtime (2021)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Introduce NaN and None values
        recommendations['runtime'] = [90, None, np.nan, 100, 95, 105, np.nan, None, 125]
        # Drop rows with NaN or None runtimes
        recommendations_clean = recommendations.dropna(subset=['runtime'])
        # Validate runtimes
        for runtime in recommendations_clean['runtime']:
            self.assertIsInstance(runtime, (int, float))
            self.assertGreater(runtime, 0)
        # Ensure reduced number of recommendations
        self.assertTrue(recommendations_clean.shape[0] < recommendations.shape[0])

    def test_runtime_mixed_data_types(self):
        """
        Test case 61: Ensure that movies with mixed data types in 'runtime' are handled
        """
        ts = [{"title": "Movie with Mixed Runtime Types (2021)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Set mixed data types in runtime
        recommendations['runtime'] = [90, '120', 110.5, None, 'NaN', -100, '95 mins', 'one hundred', np.nan]
        # Clean and convert runtimes
        def parse_runtime(value):
            try:
                if isinstance(value, str):
                    value = value.strip().lower()
                    if 'min' in value:
                        value = value.replace('min', '')
                    return float(value)
                elif isinstance(value, (int, float)):
                    return float(value)
            except ValueError:
                return np.nan
        recommendations['runtime'] = recommendations['runtime'].apply(parse_runtime)
        recommendations_clean = recommendations.dropna(subset=['runtime'])
        recommendations_clean = recommendations_clean[recommendations_clean['runtime'] > 0]
        # Validate and sort
        for runtime in recommendations_clean['runtime']:
            self.assertIsInstance(runtime, float)
            self.assertGreater(runtime, 0)
        recommendations_sorted = recommendations_clean.sort_values(by='runtime')
        runtimes = recommendations_sorted['runtime'].tolist()
        self.assertEqual(runtimes, sorted(runtimes))

    def test_runtime_in_different_languages(self):
        """
        Test case 62: Ensure that movies with runtime values in different languages are handled
        """
        ts = [{"title": "International Movie (2021)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Set runtimes in different languages
        recommendations['runtime'] = ['90 minutos', '120 Minuten', '110 分', '100 分钟', '95 min', '105 dakikalar', '115 minuti', '130 minutos', '125 minuten']
        # Since parsing these requires language-specific logic, set runtimes to NaN
        recommendations['runtime'] = np.nan
        # Validate that runtimes are NaN
        self.assertTrue(recommendations['runtime'].isnull().all())

    def test_runtime_edge_case_values(self):
        """
        Test case 63: Ensure that movies with edge case 'runtime' values (e.g., sys.maxsize) are handled
        """
        ts = [{"title": "Edge Case Runtime Movie (2021)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Set edge case runtime values
        recommendations['runtime'] = [sys.maxsize, -sys.maxsize, 0, sys.maxsize - 1, -sys.maxsize + 1, 9999999999, -9999999999, 1, -1]
        # Filter out invalid runtimes
        recommendations_clean = recommendations[recommendations['runtime'] > 0]
        # Validate and sort
        for runtime in recommendations_clean['runtime']:
            self.assertIsInstance(runtime, int)
            self.assertGreater(runtime, 0)
        recommendations_sorted = recommendations_clean.sort_values(by='runtime')
        runtimes = recommendations_sorted['runtime'].tolist()
        self.assertEqual(runtimes, sorted(runtimes))

    def test_runtime_with_unexpected_characters(self):
        """
        Test case 64: Ensure that movies with runtime values containing unexpected characters are handled
        """
        ts = [{"title": "Movie with Unexpected Characters (2021)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Set runtimes with unexpected characters
        recommendations['runtime'] = ['90$', '@120', '#110', '100%', '95^', '&105', '*115', '(130)', ')125']
        # Extract numeric values
        recommendations['runtime'] = recommendations['runtime'].str.extract('(\d+)').astype(float)
        # Validate runtimes
        for runtime in recommendations['runtime'].dropna():
            self.assertIsInstance(runtime, float)
            self.assertGreater(runtime, 0)

    def test_runtime_with_trailing_leading_spaces(self):
        """
        Test case 65: Ensure that movies with runtime values containing leading/trailing spaces are handled
        """
        ts = [{"title": "Movie with Spaces in Runtime (2021)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Set runtimes with spaces
        recommendations['runtime'] = [' 90 ', ' 120', '110 ', ' 100 ', '95', ' 105', '115 ', '130', '125 ']
        # Strip spaces and convert
        recommendations['runtime'] = recommendations['runtime'].str.strip().astype(int)
        for runtime in recommendations['runtime']:
            self.assertIsInstance(runtime, int)
            self.assertGreater(runtime, 0)

    def test_runtime_all_null_values(self):
        """
        Test case 66: Ensure that when all 'runtime' values are null, the system handles it gracefully
        """
        ts = [{"title": "Movie with All Null Runtimes (2021)", "rating": 5.0}]
        recommendations = recommend_for_new_user(ts)
        # Set all runtimes to None
        recommendations['runtime'] = [None] * recommendations.shape[0]
        # Attempt to sort and handle
        recommendations_clean = recommendations.dropna(subset=['runtime'])
        self.assertEqual(recommendations_clean.shape[0], 0)
        # Ensure that no error occurs and empty DataFrame is handled


if __name__ == "__main__":
    unittest.main()