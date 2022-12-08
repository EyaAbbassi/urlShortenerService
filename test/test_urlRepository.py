import unittest
from app import database as db
from app.util import urlRepository


class testUrlRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # run once before all test cases ###
        print("setUpClass\n")

    @classmethod
    def tearDownClass(cls):  # run once after all test cases ###
        print("tearDownClass\n")

    def setUp(self):  # run before each test case ###
        print("setUp\n")
        self.long_to_short = {
            "https://mail.google.com/": "http://short.ner/q4QFrylh",
            "https://calendar.google.com/calendar/u/0/r/week": "http://short.ner/custom"
        }
        self.short_to_long = {
            "q4QFrylh": "https://mail.google.com/",
            "custom": "https://calendar.google.com/calendar/u/0/r/week"
        }
        self.base_URL = "http://short.ner/"
        self.mockData = db.Database(self.long_to_short, self.short_to_long)
        self.repo = urlRepository.Repository(self.mockData)

    def tearDown(self):  # run after each test case ###
        print("tearDown\n")

    def test_get_base_url(self):
        print("test_get_base_url\n")
        result = self.repo.get_base_URL()
        self.assertEqual(result, self.mockData.base_URL)

    def test_get_len_base_URL(self):
        print("test_get_len_base_URL\n")
        result = self.repo.get_len_base_URL()
        base_url = self.repo.get_base_URL()
        self.assertEqual(result, len(base_url))

    def test_is_exist_key_should_return_True(self):
        print("test_is_exist_key_should_return_True\n")
        key = "custom"
        result = self.repo.is_exist_key(key)
        self.assertTrue(result)

    def test_is_exist_key_should_return_False(self):
        print("test_is_exist_key_should_return_False\n")
        key = "RTY78U52"
        result = self.repo.is_exist_key(key)
        self.assertFalse(result)

    def test_is_exist_url_where_url_exist_should_return_True(self):
        print("test_is_exist_url_where_url_exist_should_return_True\n")
        url = "https://mail.google.com/"
        result = self.repo.is_exist_url(url)
        self.assertTrue(result)

    def test_is_exist_url_where_url_doesnt_exist_should_return_False(self):
        print("test_is_exist_url_where_url_doesnt_exist_should_return_False\n")
        url = "https://seanprashad.com/leetcode-patterns/"
        result = self.repo.is_exist_key(url)
        self.assertFalse(result)

    def test_get_long_URL_where_short_url_exist_should_return_correspond_origin_url(self):
        print(
            "test_get_long_URL_where_short_url_exist_should_return_correspond_origin_url\n")
        short_key = "custom"
        result_exist = self.repo.get_long_URL(short_key)
        self.assertEqual(
            result_exist, "https://calendar.google.com/calendar/u/0/r/week")

    def test_get_long_URL_where_short_url_doesnt_exist_should_return_None(self):
        print(
            "test_get_long_URL_where_short_url_doesnt_exist_should_return_correspond_origin_url\n")
        result_notFound = self.repo.is_exist_key("https://instagram.com/")
        self.assertFalse(result_notFound)

    def test_get_short_URL_where_long_url_exist_should_return_correspond_short_url(self):
        print(
            "test_get_long_URL_where_short_url_doesnt_exist_should_return_correspond_origin_url\n")
        original_url = "https://mail.google.com/"
        result_exist = self.repo.get_short_URL(original_url)
        self.assertEqual(result_exist, "http://short.ner/q4QFrylh")

    def test_get_short_URL_where_long_url_doesnt_exist_should_return_None(self):
        print(
            "test_get_short_URL_where_long_url_doesnt_exist_should_return_None\n")
        result_notFound = self.repo.is_exist_key("test")
        self.assertFalse(result_notFound)

    def test_save_data_where_inputs_doesnt_exist(self):
        print("test_save_data_where_inputs_doesnt_exist\n")
        url = "https://www.instagram.com/"
        generated_key = "8PM4Hyz8"
        url_and_key_exist = self.repo.is_exist_key(
            generated_key) and self.repo.is_exist_url(url)
        if not url_and_key_exist:
            result = self.repo.save_url(url, generated_key)
        self.assertTrue(result)

    def test_save_data_where_inputs_are_valid_should_return_None(self):
        print("test_save_data_where_inputs_are_valid_should_return_nothing\n")
        url = "https://mail.google.com/"
        generated_key = "q4QFrylh"
        url_and_key_exist = self.repo.is_exist_key(
            generated_key) and self.repo.is_exist_url(url)
        if url_and_key_exist:
            result = self.repo.save_url(url, generated_key)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
