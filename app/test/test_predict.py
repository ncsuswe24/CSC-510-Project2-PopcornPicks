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


if __name__ == "__main__":
    unittest.main()