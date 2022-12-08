from flask import jsonify
from app import database


class Repository:

    def __init__(self, data=database.Database()) -> None:
        self.data = data

    def get_base_URL(self):
        return self.data.base_URL

    def get_len_base_URL(self):
        return len(self.data.base_URL)

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
        # jsonify({
        #     'status': 'error',
        #     'message': 'The given short URL doesn\'t exist!'
        # }), 404

    def get_short_URL(self, original_url):
        if self.is_exist_url(original_url):
            return self.data.long_to_short[original_url]
        return jsonify({
            'status': 'error',
            'message': 'The given original URL doesn\'t exist!'
        }), 404

    def save_url(self, url: str, generated_key: str):
        if self.is_exist_key(generated_key) or self.is_exist_url(url):
            return None
            # jsonify({
            #     'status': 'error',
            #     'message': 'The given original URL or key already saved in the database'
            # }), 400

        self.data.long_to_short[url] = self.data.base_URL + generated_key
        self.data.short_to_long[generated_key] = url
        return True
