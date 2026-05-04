import unittest
import os
import sys
from unittest.mock import patch, MagicMock
import requests

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from crawler import crawl

class TestCrawler(unittest.TestCase):

    """
    Tests the crawler module for correctness and edge cases,
    using mocked HTTP requests to avoid hitting the real website during testing.   
    """

    def setUp(self):
        self.fake_html_with_next = """
        <html>
            <body>
                <p>Page content</p>
                <li class="next"><a href="/page/2/">Next</a></li>
            </body>
        """

        self.fake_html_without_next = """
        <html>
            <body>
                <p>Last page content</p>
            </body>
        </html>            
        """

    @patch('crawler.requests.get')
    def test_crawl_with_one_page(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = self.fake_html_without_next
        mock_get.return_value = mock_response

        result = crawl("https://quotes.toscrape.com", delay=0)
        self.assertIn("https://quotes.toscrape.com/page/1/", result)
        self.assertEqual(len(result), 1)

    @patch('crawler.requests.get')
    def test_crawl_with_multiple_pages(self, mock_get):
        mock_response1 = MagicMock()
        mock_response1.text = self.fake_html_with_next

        mock_response2 = MagicMock()
        mock_response2.text = self.fake_html_without_next

        mock_get.side_effect = [mock_response1, mock_response2]

        result = crawl("https://quotes.toscrape.com", delay=0)
        self.assertIn("https://quotes.toscrape.com/page/1/", result)
        self.assertEqual(len(result), 2)        

    @patch('crawler.requests.get')
    def test_crawl_returns_text(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = self.fake_html_without_next
        mock_get.return_value = mock_response

        result = crawl("https://quotes.toscrape.com", delay=0)
        page_text = result["https://quotes.toscrape.com/page/1/"]
        self.assertIsNotNone(page_text)
        self.assertGreater(len(page_text), 0)        

    @patch('crawler.requests.get')
    def test_crawl_with_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError
        result = crawl("https://quotes.toscrape.com", delay=0)
        self.assertEqual(result, {})

    @patch('crawler.requests.get')
    def test_crawl_with_request_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException
        result = crawl("https://quotes.toscrape.com", delay=0)
        self.assertEqual(result, {})   

    @patch('crawler.requests.get')
    def test_crawl_empty_base_url(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException
        result = crawl("", delay=0)
        self.assertEqual(result, {})                      