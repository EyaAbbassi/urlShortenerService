import requests
import unittest


class testUrlRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # run once before all test cases ###
        print("setUpClass\n")

    @classmethod
    def tearDownClass(cls):  # run once after all test cases ###
        print("tearDownClass\n")

    def setUp(self):  # run before each test case ###
        print("setUp\n")
        self.url = ("http://127.0.0.1:5000/decode")

    def tearDown(self):  # run after each test case ###
        print("tearDown\n")


if __name__ == '__main__':
    unittest.main()
