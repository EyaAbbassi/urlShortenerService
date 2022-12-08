from random import choice
import string
from app.util import urlRepository
url_tools = urlRepository.Repository()


class RandomGenerator:

    def __init__(self, num_of_chars=8) -> None:
        self.num_of_chars = num_of_chars

    def generate_random_key(self):
        """Function to generate random_key of specified number of characters"""
        generated_random_key = ''.join(
            choice(string.ascii_letters+string.digits) for _ in range(self.num_of_chars))
        while url_tools.is_exist_key(generated_random_key):
            self.generate_random_key(self.num_of_chars)
        return generated_random_key
