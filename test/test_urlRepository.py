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

    def test_is_exist_key(self, key="custom"):
        print("test_is_exist_key\n")
        result = self.repo.is_exist_key(key)
        self.assertTrue(result)
        key = "RTY78U52"
        result = self.repo.is_exist_key(key)
        self.assertFalse(result)

    def test_is_exist_url(self, url="https://mail.google.com/"):
        print("test_is_exist_url\n")
        result = self.repo.is_exist_url(url)
        self.assertTrue(result)
        unavailable_url = "https://seanprashad.com/leetcode-patterns/"
        result = self.repo.is_exist_key(unavailable_url)
        self.assertFalse(result)

    def test_get_long_URL(self, short_key="custom"):
        print("test_get_long_URL\n")
        result_exist = self.repo.get_long_URL(short_key)
        result_notFound = self.repo.is_exist_key("https://instagram.com/")
        self.assertEqual(
            result_exist, "https://calendar.google.com/calendar/u/0/r/week")
        self.assertFalse(result_notFound)

    def test_get_short_URL(self, original_url="https://mail.google.com/"):
        print("test_get_short_URL\n")
        result_exist = self.repo.get_short_URL(original_url)
        result_notFound = self.repo.is_exist_key("test")
        self.assertEqual(result_exist, "http://short.ner/q4QFrylh")
        self.assertFalse(result_notFound)

    def test_save_url(self, url="https://www.instagram.com/", generated_key="8PM4Hyz8"):
        print("test_save_url\n")
        self.mockData.long_to_short[url] = self.mockData.base_URL + \
            generated_key
        self.mockData.short_to_long[generated_key] = url
        result = self.repo.is_exist_key(
            generated_key) and self.repo.is_exist_url(url)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
