import unittest
import sys
import os
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from indexer import index, save_index, load_index

class TestIndexer(unittest.TestCase):
    def setUp(self):
        self.pages = {
            "https://quotes.toscrape.com/page/1/": "The world is good and life is good",
            "https://quotes.toscrape.com/page/2/": "Life is beautiful",
            "https://quotes.toscrape.com/page/3/": "The world is beautiful"
        }
        self.index_data = index(self.pages)

    def test_word_across_pages(self):
        word = "life"
        self.assertIn("https://quotes.toscrape.com/page/1/", self.index_data[word])
        self.assertIn("https://quotes.toscrape.com/page/2/", self.index_data[word])

    def test_empty_pages(self):
        empty_pages = {}
        empty_index = index(empty_pages)
        self.assertEqual(empty_index, {})

    def test_word_frequency(self):
        word = "good"
        expected_frequency = 2
        page = "https://quotes.toscrape.com/page/1/"
        actual_frequency = self.index_data[word][page]["frequency"]
        self.assertEqual(actual_frequency, expected_frequency)

    def test_word_positions(self):
        word = "good"
        expected_positions = [3, 7]
        page = "https://quotes.toscrape.com/page/1/"
        actual_positions = self.index_data[word][page]["positions"]
        self.assertEqual(actual_positions, expected_positions)

    def test_case_insensitivity(self):
        self.assertIn("the", self.index_data)
        self.assertNotIn("The", self.index_data)

    def test_save_and_load(self):
        filepath = tempfile.mktemp()
        save_index(self.index_data, filepath)
        result = load_index(filepath)
        self.assertEqual(result, self.index_data)

    def test_save_empty_index(self):
        empty_index = {}
        filepath = tempfile.mktemp()
        save_index(empty_index, filepath)
        result = load_index(filepath)
        self.assertEqual(result, empty_index)

    def test_invalid_filepath_save(self):
        with self.assertRaises(Exception):
            save_index({}, "/invalid/path/index.json")

    def test_invalid_filepath_load(self):
        with self.assertRaises(Exception):
            load_index("/invalid/path/index.json")            