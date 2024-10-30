"""
Copyright (c) 2023 Abhinav Sinha, Chandana Ray, Sam Kwiatkowski-Martin, Tanmay Pardeshi
This code is licensed under MIT license (see LICENSE for details)

@author: PopcornPicks

Test suit for search feature
"""

import sys
import unittest
import warnings
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.search import Search

warnings.filterwarnings("ignore")

class Tests(unittest.TestCase):
    """
    Test cases for search feature
    """

    def test_search_single_complete_word_match(self):
        """
        Test case 1: Single complete word that matches a title exactly
        """
        search_word = "Titanic"
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = [
            'Titanic (1997)', 
            'Titanic (1953)', 
            'Titanica (1995)', 
            'Titanic Town (1998)', 
            'Titanic (1996)', 
            'Titanic: The Final Word with James Cameron (2012)', 
            'Titanic 2 (2010)', 
            'The Chambermaid on the Titanic (1997)', 
            'Raise the Titanic (1980)', 
            'The Ten Lives of Titanics the Cat (2007)'
            ]
        self.assertTrue(filtered_dict == expected_resp)
    
    def test_search_single_partial_word_match(self):
        """
        Test case 2: Single incomplete word that partially matches a title
        """
        search_word = "Avat"  # Should match titles like "Avatar"
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = [
            'Avatar (2009)', 
            'Avatar 2 (2020)', 
            'Avatar: Creating the World of Pandora (2010)', 
            'My Avatar and Me (2010)'
        ]
        self.assertTrue(filtered_dict == expected_resp)

    def test_search_single_word_year_match(self):
        """
        Test case 3: Single word that is a year
        """
        search_word = "1994"  # Should return movies released in 1994
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = [
            'Guardian Angel (1994)', 
            'Lamerica (1994)', 
            'The Postman (1994)', 
            'Shopping (1994)', 
            'Nobody Loves Me (1994)', 
            'Chungking Express (1994)', 
            'The Neverending Story III: Escape from Fantasia (1994)', 
            'The Silences of the Palace (1994)', 
            'Amateur (1994)', 
            'Crumb (1994)'
            ]
        self.assertTrue(filtered_dict == expected_resp)
    
    def test_search_gibberish_single_word(self):
        """
        Test case 4: Single gibberish word that should return no results
        """
        search_word = "worodowo"
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = []
        self.assertTrue(filtered_dict == expected_resp)

    def test_search_two_complete_words(self):
        """
        Test case 5: Two complete words that match parts of a title
        """
        search_word = "Star Wars"
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = [
            'Star Wars (1977)', 
            'Star Wars: Episode I - The Phantom Menace (1999)', 
            'Star Wars: Episode II - Attack of the Clones (2002)', 
            'Star Wars: Episode III - Revenge of the Sith (2005)', 
            'Star Wars: The Clone Wars (2008)', 
            'Star Wars: The Force Awakens (2015)', 
            'Empire of Dreams: The Story of the Star Wars Trilogy (2004)', 
            'The Star Wars Holiday Special (1978)', 
            'Robot Chicken: Star Wars (2007)', 
            'Plastic Galaxy: The Story of Star Wars Toys (2014)'
            ]

        self.assertTrue(filtered_dict == expected_resp)
    
    def test_search_two_words_one_partial(self):
        """
        Test case 6: Two words, one is incomplete
        """
        search_word = "Harry Po"  # Should match "Harry Potter" titles
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = [
            "Harry Potter and the Philosopher's Stone (2001)", 
            'Harry Potter and the Chamber of Secrets (2002)', 
            'Harry Potter and the Prisoner of Azkaban (2004)', 
            'Harry Potter and the Goblet of Fire (2005)', 
            'Harry Potter and the Order of the Phoenix (2007)', 
            'Harry Potter and the Half-Blood Prince (2009)', 
            'Harry Potter and the Deathly Hallows: Part 1 (2010)', 
            'Harry Potter and the Deathly Hallows: Part 2 (2011)', 
            'Harry in Your Pocket (1973)', 
            'When Harry Met Sally... (1989)'
        ]

        self.assertTrue(filtered_dict == expected_resp)

    def test_search_title_with_year(self):
        """
        Test case 7: Full title with a year
        """
        search_word = "The Matrix 1999"
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = [
            'The Matrix (1999)', 
            'The Matrix Reloaded (2003)', 
            'The Matrix Revolutions (2003)', 
            'Class of 1999 II - The Substitute (1994)', 
            'Return to Source: The Philosophy of The Matrix (2004)', 
            'The Matrix Revisited (2001)', 
            'The Theory of Flight (1999)', 
            'The 24 Hour Woman (1999)', 
            'Blast from the Past (1999)', 
            'The Other Sister (1999)'
            ]
        self.assertTrue(filtered_dict == expected_resp)

    def test_search_start_of_title(self):
        """
        Test case 8: Word that matches the start of titles
        """
        search_word = "Harry"  
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = [
            'Harry and the Hendersons (1987)', 
            "Harry, He's Here To Help (2000)", 
            "Harry Potter and the Philosopher's Stone (2001)", 
            'Harry and Walter Go To New York (1976)', 
            'Harry Potter and the Chamber of Secrets (2002)', 
            'Harry Potter and the Prisoner of Azkaban (2004)', 
            'Harry and Tonto (1974)', 
            'Harry Potter and the Goblet of Fire (2005)', 
            'Harry Potter and the Order of the Phoenix (2007)', 
            'Harry Potter and the Half-Blood Prince (2009)'
        ]

        self.assertTrue(filtered_dict == expected_resp)

    def test_search_partial_word_start_of_word(self):
        """
        Test case 9: Partial word at the start of a title word
        """
        search_word = "Trans"  # Partial match for "Pirates" in "Pirates of the Caribbean"
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = [
            'Trans (1998)', 
            'Transylvania 6-5000 (1985)', 
            'Transporter 2 (2005)', 
            'Transamerica (2005)', 
            'Transformers (2007)', 
            'Transsiberian (2008)', 
            'Transporter 3 (2008)', 
            'Transformers: Revenge of the Fallen (2009)', 
            'Transylmania (2009)', 
            'Trans-Europ-Express (1966)'
        ]
        self.assertTrue(filtered_dict == expected_resp)

    def test_search_middle_word_in_title(self):
        """
        Test case 10: Single word that appears in the middle of the word
        """
        search_word = "utur"  # Matches titles like "Back to the Future"
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = [
            'Suture (1993)', 
            'Back to the Future (1985)', 
            'Back to the Future Part II (1989)', 
            'Back to the Future Part III (1990)', 
            'Yor, the Hunter from the Future (1983)', 
            'Bright Future (2003)', 
            'Futureworld (1976)', 
            'Woman Is the Future of Man (2004)', 
            "Futurama: Bender's Big Score (2007)", 
            'Future by Design (2006)'
        ]
        self.assertTrue(filtered_dict == expected_resp)

    def test_search_nonexistent_word(self):
        """
        Test case 11: 3 words that does not match any title
        """
        search_word = "Not single title"
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = [
            'Maybe... Maybe Not (1994)', 
            'To Be or Not to Be (1942)', 
            'A Single Girl (1995)', 
            "I'm Not Rappaport (1996)", 
            'I Love You, I Love You Not (1996)', 
            'Experience Preferred...But Not Essential (1982)', 
            'The World Is Not Enough (1999)', 
            'Not Love, Just Frenzy (1996)', 
            'Single White Female (1992)', 
            'Not One Less (1999)'
            ]
        self.assertTrue(filtered_dict == expected_resp)

    def test_search_three_words_in_title(self):
        """
        Test case 12: Three complete words that match parts of a title
        """
        search_word = "Lord of Rings"
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = [
            'The Lord of the Rings (1978)', 
            'The Lord of the Rings: The Fellowship of the Ring (2001)', 
            'The Lord of the Rings: The Two Towers (2002)', 
            'The Lord of the Rings: The Return of the King (2003)', 
            'Lord of Illusions (1995)', 
            'Lord of the Flies (1963)', 
            'Phantasm III: Lord of the Dead (1994)', 
            'Lord of the Flies (1990)', 
            'Greystoke: The Legend of Tarzan, Lord of the Apes (1984)', 
            'At Play in the Fields of the Lord (1991)'
        ]
        self.assertTrue(filtered_dict == expected_resp)
    
    def test_search_partial_match_with_multiple_words(self):
        """
        Test case 13: Three words, one is incomplete one with year
        """
        search_word = "Beauty 1994 Bea"
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = [
            'Black Beauty (1994)', 
            'Beauty and the Beast (1991)', 
            'Stealing Beauty (1996)', 
            'Sleeping Beauty (1959)', 
            'Dangerous Beauty (1998)', 
            'American Beauty (1999)', 
            'Fatal Beauty (1987)', 
            'The Object of Beauty (1991)', 
            'Beauty and the Beast (1946)', 
            'Stage Beauty (2004)'
        ]
        self.assertTrue(filtered_dict == expected_resp)

    def test_search_title_with_only_year(self):
        """
        Test case 14: 3 words with only incomplete word
        """
        search_word = "Last ai ben"
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = [
            'The Last Airbender (2010)', 
            'The Last Detail (1973)', 
            'FernGully: The Last Rainforest (1992)', 
            'The Last Samurai (2003)', 
            'Last Train from Gun Hill (1959)', 
            'Last Train Home (2009)', 
            'The Last Mountain (2011)', 
            'Last Train to Freo (2006)', 
            'The Staircase II: The Last Chance (2012)', 
            'The Last Straight Man (2014)'
            ]
        self.assertTrue(filtered_dict == expected_resp)

    def test_search_gibberish_multiple_words(self):
        """
        Test case 15: Multiple gibberish words that should return no results
        """
        search_word = "woedow foas feow"
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = []  
        self.assertTrue(filtered_dict == expected_resp)

    def test_search_start_of_word_with_two_partial_words(self):
        """
        Test case 16: Two partial words at the start of title words
        """
        search_word = "Hu ga"  # Partial matches for "Hunger Games" or "Finding Nemo"
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = [
            'Jiang Hu (2004)', 
            'Hunting and Gathering (2007)', 
            'The Hunger Games (2012)', 
            'The Hunger Games: Catching Fire (2013)', 
            'The Hunger Games: Mockingjay - Part 1 (2014)', 
            'The Hungover Games (2014)', 
            'The Hunger Games: Mockingjay - Part 2 (2015)', 
            'Galaxy Hunter (2004)', 
            "Gabriel Iglesias: I'm Sorry for What I Said When I Was Hungry (2016)", 
            'Hunter Gatherer (2016)'
            ]
        self.assertTrue(filtered_dict == expected_resp)

    def test_search_misspell_one_word(self):
        """
        Test case 17: Common title with a typo
        """
        search_word = "Interstller"  # Should attempt matching "Interstellar"
        finder = Search()
        corrected = finder.correct_spelling(search_word)
        expected_spelling = "interstellar"
        self.assertTrue(corrected == expected_spelling)

    def test_search__misspell_long_word(self):
        """
        Test case 18: Long phrase including partial word and year
        """
        search_word = "Hungar gamm"
        finder = Search()
        finder = Search()
        corrected = finder.correct_spelling(search_word)
        expected_spelling = "hunger game"
        self.assertTrue(corrected == expected_spelling)
    def test_search_lower(self):
        """
        Test case 19: lowercase 1 word
        """
        search_word = "toy"
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = [
            "Toy Story (1995)",
            "Toys (1992)",
            "Toy Story 2 (1999)",
            "Toy Soldiers (1991)",
            "Toy Story 3 (2010)",
            "Toys in the Attic (1963)",
            "Toy Story of Terror! (2013)",
            "Toy Story That Time Forgot (2014)",
            "Toys in the Attic (2009)",
            "Toy Soldiers (1984)"
        ]
        self.assertTrue(filtered_dict == expected_resp)
    def test_search_UPPER(self):
        """
        Test case 20: lower case with 2 words
        """
        search_word = "LOVE"
        finder = Search()
        filtered_dict = finder.results_top_ten(search_word)
        expected_resp = [
            "Love & Human Remains (1993)",
            "Love Affair (1994)",
            "Love and a .45 (1994)",
            "Lover's Knot (1996)",
            "Love in the Afternoon (1957)",
            "Love Is All There Is (1996)",
            "Love Jones (1997)",
            "Love and Other Catastrophes (1996)",
            "Love! Valour! Compassion! (1997)",
            "Love Serenade (1996)",
        ]
        self.assertTrue(filtered_dict == expected_resp)


if __name__ == "__main__":
    unittest.main()
