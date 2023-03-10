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
        self.encodeUrl = ("http://127.0.0.1:5000/encode")
        self.decodeUrl = ("http://127.0.0.1:5000/decode")

    def tearDown(self):  # run after each test case ###
        print("tearDown\n")

    def test_encodeAPI_with_valid_data_should_return_OK(self):
        print("test_encodeAPI_with_valid_data_should_return_OK\n")
        data = {"long_url": "https://facebook.com/test", "custom_id": ""}
        request = requests.post(self.encodeUrl, json=data)
        self.assertEqual((request.status_code, request.reason), (200, "OK"))

    def test_encodeAPI_with_valid_data_and_custom_key_should_return_OK(self):
        print("test_encodeAPI_with_valid_data_and_custom_key_should_return_OK\n")
        # correct input with custom key
        data = {"long_url": "https://www.google.com/docs",
                "custom_id": "YH86PEK1"}
        request = requests.post(self.encodeUrl, json=data)
        self.assertEqual((request.status_code, request.reason), (200, "OK"))

    def test_encodeAPI_with_empty_url_should_return_BAD_REQUEST(self):
        print("test_encodeAPI_with_empty_url_should_return_BAD_REQUEST\n")
        # empty url
        data = {"long_url": "", "custom_id": ""}
        request = requests.post(self.encodeUrl, json=data)
        self.assertEqual(
            (request.status_code, request.reason), (400, 'BAD REQUEST'))

    def test_encodeAPI_with_unvalid_url_should_return_BAD_REQUEST(self):
        print("test_encodeAPI_with_unvalid_url_should_return_BAD_REQUEST\n")
        # unvalid url
        data = {"long_url": "http://this/is/invalid", "custom_id": ""}
        request = requests.post(self.encodeUrl, json=data)
        self.assertEqual(
            (request.status_code, request.reason), (400, 'BAD REQUEST'))

    def test_encodeAPI_with_existing_url_should_return_OK(self):
        print("test_encodeAPI_with_existing_url_should_return_OK\n")
        # already existing url with custom key => should be updated
        data = {"long_url": "https://www.google.com/docs", "custom_id": ""}
        request = requests.post(self.encodeUrl, json=data)
        self.assertEqual(
            (request.status_code, request.reason), (200, "OK"))

    def test_encodeAPI_with_existing_url_and_added_key_should_be_update_then_return_OK(self):
        print("test_encodeAPI_with_existing_url_and_added_key_should_be_update_then_return_OK\n")
        data = {"long_url": "https://www.google.com/docs",
                "custom_id": "Updat6e"}
        request = requests.post(self.encodeUrl, json=data)
        self.assertEqual(
            (request.status_code, request.reason), (200, "OK"))

    def test_decodeAPI_with_existing_short_url_should_return_OK(self):
        print("test_decodeAPI_with_valid_data_should_return_OK\n")
        data = {"short_url": "http://short.ner/YH86PEK1"}
        request = requests.get(self.decodeUrl, json=data)
        self.assertEqual((request.status_code, request.reason), (200, "OK"))

    def test_decodeAPI_with_non_existing_short_url_should_return_NOT_FOUND(self):
        print("test_decodeAPI_with_non_existing_short_url_should_return_NOT_FOUND\n")
        data = {"short_url": "http://short.ner/notFound"}
        request = requests.get(self.decodeUrl, json=data)
        self.assertEqual((request.status_code, request.reason),
                         (404, "NOT FOUND"))

    def test_decodeAPI_with_unvalid_short_url_should_return_BAD_REQUEST(self):
        print("test_decodeAPI_with_unvalid_short_url_should_return_BAD_REQUEST\n")
        data = {"short_url": "http://short.ner/"}
        request = requests.get(self.decodeUrl, json=data)
        self.assertEqual((request.status_code, request.reason),
                         (400, "BAD REQUEST"))

    def test_decodeAPI_with_empty_url_should_return_BAD_REQUEST(self):
        print("test_decodeAPI_with_empty_url_should_return_BAD_REQUEST\n")
        # empty url
        data = {"short_url": ""}
        request = requests.get(self.decodeUrl, json=data)
        self.assertEqual(
            (request.status_code, request.reason), (400, 'BAD REQUEST'))


if __name__ == '__main__':
    unittest.main()
