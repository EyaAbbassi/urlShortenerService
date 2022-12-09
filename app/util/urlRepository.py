from app import database
from app.util import RandomGenerator


class Repository:

    def __init__(self, data=database.Database()) -> None:
        self.data = data

    def get_base_URL(self):
        return self.data.base_URL

    def get_len_base_URL(self):
        return len(self.data.base_URL)

    def get_key(self, short_url):
        base_url_len = self.get_len_base_URL()
        if len(short_url) > base_url_len:
            return short_url[base_url_len:]
        return None

    def is_valid_short_url(self, short_url):
        if self.get_key(short_url):
            return True
        return False

    def is_exist_key(self, key):
        if key in self.data.short_to_long:
            return True
        return False

    def is_exist_url(self, url):
        if url in self.data.long_to_short:
            return True
        return False

    def get_long_URL(self, short_key):
        if self.is_exist_key(short_key):
            return self.data.short_to_long[short_key]
        return None

    def get_short_URL(self, original_url):
        if self.is_exist_url(original_url):
            return self.data.long_to_short[original_url]
        return None

    def save_url(self, url, key):
        if self.is_exist_key(key) and self.is_exist_url(url):
            return
        elif self.is_exist_url(url):
            old_short_url = self.get_short_URL(url)
            old_key = self.get_key(old_short_url)
            del self.data.short_to_long[old_key]
            del self.data.long_to_short[url]

        self.data.long_to_short[url] = self.data.base_URL + key
        self.data.short_to_long[key] = url
        return True
