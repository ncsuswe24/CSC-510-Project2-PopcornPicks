"""
Copyright (c) 2023 Abhinav Sinha, Chandana Ray, Sam Kwiatkowski-Martin, Tanmay Pardeshi
This code is licensed under MIT license (see LICENSE for details)

@author: PopcornPicks
"""
import os
import pandas as pd
#from flask import jsonify, request, render_template
from spellchecker import SpellChecker


app_dir = os.path.dirname(os.path.abspath(__file__))
code_dir = os.path.dirname(app_dir)
project_dir = os.path.dirname(code_dir)


class Search:
    """
    Search feature for landing page
    """

    df = pd.read_csv(project_dir + "/data/movies.csv")

    def __init__(self):
        pass

    def starts_with(self, word):
        """
        Function to check movie prefix
        """
        n = len(word)
        res = []
        word = word.lower()
        for x in self.df["title"]:
            curr = x.lower()
            if curr[:n] == word:
                res.append(x)
        return res
    def correct_spelling(self,input_text):
        """
        Function to correct misspelled words
        """
        spell = SpellChecker()
        words = input_text.split()
        corrected_words = [
            spell.correction(word)
            if spell.unknown([word])
            else word for word in words
            ]
        return " ".join(corrected_words)

    def anywhere(self, words, visited_words):
        """
        Function to check visited words
        """
        res = []
        movie_dict={}
        words=words.lower().strip().split(" ")
        for x in self.df["title"]:
            if x not in visited_words:
                curr = x.lower().strip().split(" ")
                score=0
                for w in words:
                    half=False
                    quarter=False
                    full=False
                    for w_curr in curr:
                        if w in w_curr:
                            quarter=True
                        if w_curr.startswith(w):
                            half=True
                        if  w == w_curr :
                            full=True
                            break
                    if full:
                        score+=1
                    elif half:
                        score+=0.2
                    elif quarter:
                        score+=0.1
                movie_dict[x]=score
        filtered_dict = {k: v for k, v in movie_dict.items() if v != 0}
        sorted_dict = dict(sorted(filtered_dict.items(), key=lambda item: item[1],reverse=True))
        res=sorted_dict.keys()
        return res

    def results(self, word):
        """
        Function to serve the result render
        """
        starts_with = self.starts_with(word)
        visited_words = set()
        for x in starts_with:
            visited_words.add(x)
        anywhere = self.anywhere(word, visited_words)
        starts_with.extend(anywhere)
        return starts_with

    def results_top_ten(self, word):
        """
        Function to get top 10 results
        """
        return self.results(word)[:10]


#if __name__ == "__main__":
#    app.run()
