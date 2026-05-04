import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from search import print_results, find_word

class TestSearch(unittest.TestCase):

    """
    Tests the search module for correctness and edge cases,
    using a mock inverted index.  
    """

    def setUp(self):
        self.index_data = {
            "world": {
                "https://quotes.toscrape.com/page/1/": {"frequency": 1, "positions": [1]},
                "https://quotes.toscrape.com/page/3/": {"frequency": 1, "positions": [1]}
            },
            "life": {
                "https://quotes.toscrape.com/page/1/": {"frequency": 1, "positions": [4]},
                "https://quotes.toscrape.com/page/2/": {"frequency": 1, "positions": [1]}
            },
            "good": {
                "https://quotes.toscrape.com/page/1/": {"frequency": 2, "positions": [3, 7]}
            },
            "beautiful": {
                "https://quotes.toscrape.com/page/2/": {"frequency": 1, "positions": [2]},
                "https://quotes.toscrape.com/page/3/": {"frequency": 1, "positions": [2]}
            }                
        }

    def test_find_word_single(self):
        results = find_word(self.index_data, "world") 
        expected = {
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/3/"
        }
        self.assertEqual(results, expected)

    def test_find_word_multiple(self):
        results = find_word(self.index_data, "world life")      
        expected = {
            "https://quotes.toscrape.com/page/1/"
        }  
        self.assertEqual(results, expected)

    def test_find_word_nonexistent(self):
        results = find_word(self.index_data, "nonexistent")
        self.assertIsNone(results)

    def test_find_word_empty(self):
        results = find_word(self.index_data, "")
        self.assertIsNone(results)

    def test_find_word_no_common_pages(self):
        results = find_word(self.index_data, "good beautiful")
        self.assertIsNone(results)

    def test_find_word_case_insensitivity(self):
        results = find_word(self.index_data, "WORLD")
        expected = {
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/3/"
        }
        self.assertEqual(results, expected)  

    def test_print_results_word_nonexistent(self):
        results = print_results(self.index_data, "nonexistent")
        self.assertIsNone(results)

          