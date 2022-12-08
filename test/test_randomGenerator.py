import unittest
from app import database as db
from app.util import RandomGenerator, urlRepository


class testUrlRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # run once before all test cases ###
        print("setUpClass\n")

    @classmethod
    def tearDownClass(cls):  # run once after all test cases ###
        print("tearDownClass\n")

    def setUp(self):  # run before each test case ###
        print("setUp\n")
        self.short_to_long = {
            "q4QFrylh": "https://mail.google.com/",
            "custom": "https://calendar.google.com/calendar/u/0/r/week"
        }
        self.mockData = db.Database({}, self.short_to_long)
        self.repo = urlRepository.Repository(self.mockData)
        self.randomGenerator = RandomGenerator.RandomGenerator()
        self.num_of_chars = self.randomGenerator.num_of_chars

    def tearDown(self):  # run after each test case ###
        print("tearDown\n")

    def test_generate_random_key(self):
        print("test_generate_random_key\n")
        generated_random = self.randomGenerator.generate_random_key()
        existing_random = "q4QFrylh"
        len_generated = len(generated_random)
        result_generated = self.repo.is_exist_key(generated_random)
        result_existing = self.repo.is_exist_key(existing_random)
        self.assertFalse(result_generated)
        self.assertTrue(result_existing)
        self.assertEqual(len_generated, self.num_of_chars)


if __name__ == '__main__':
    unittest.main()
